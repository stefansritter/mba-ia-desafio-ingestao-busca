import os
from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_postgres import PGVector
from langchain.prompts import ChatPromptTemplate

load_dotenv()

def search_prompt(prompt: str) -> str:

    embeddings = OpenAIEmbeddings(model=os.getenv("OPENAI_EMBEDDING_MODEL", "text-embedding-3-small"))

    store = PGVector(
        embeddings=embeddings,
        collection_name=os.getenv("PG_VECTOR_COLLECTION_NAME"),
        connection=os.getenv("DATABASE_URL"),
        use_jsonb=True
    )

    query = prompt

    results = store.similarity_search_with_score(query, k=10)

    context = ""
    for i, (doc, score) in enumerate(results, start=1):
        context += "\n\nResultado " + str(i) + " (Score: " + str(round(score, 2)) + "):\n\n"
        context += doc.page_content.strip()

    PROMPT_TEMPLATE = """
    CONTEXTO:
    {contexto}

    REGRAS:
    - Responda somente com base no CONTEXTO.
    - Se a informação não estiver explicitamente no CONTEXTO, responda:
        "Não tenho informações necessárias para responder sua pergunta."
    - Nunca invente ou use conhecimento externo.
    - Nunca produza opiniões ou interpretações além do que está escrito.

    EXEMPLOS DE PERGUNTAS FORA DO CONTEXTO:
    Pergunta: "Qual é a capital da França?"
    Resposta: "Não tenho informações necessárias para responder sua pergunta."

    Pergunta: "Quantos clientes temos em 2024?"
    Resposta: "Não tenho informações necessárias para responder sua pergunta."

    Pergunta: "Você acha isso bom ou ruim?"
    Resposta: "Não tenho informações necessárias para responder sua pergunta."

    PERGUNTA DO USUÁRIO:
    {pergunta}

    RESPONDA A "PERGUNTA DO USUÁRIO"
    """

    user = ("user", PROMPT_TEMPLATE)
    chat_prompt = ChatPromptTemplate([user])
    prompt = chat_prompt.format_messages(contexto={context}, pergunta={query})

    llm = ChatOpenAI(model=os.getenv("OPENAI_LLM_MODEL"), temperature=0.2)
    chain = ChatPromptTemplate.from_template("{input}") | llm
    resp = chain.invoke({"input": prompt})
    return resp.content

if __name__ == "__main__":
    search_prompt()