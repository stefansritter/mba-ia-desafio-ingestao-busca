import os
from dotenv import load_dotenv
from search import search_prompt

load_dotenv()

def main():

    for k in ("OPENAI_API_KEY", "OPENAI_LLM_MODEL", "OPENAI_EMBEDDING_MODEL", "DATABASE_URL", "PG_VECTOR_COLLECTION_NAME", "PDF_PATH"):
        if not os.getenv(k):
            raise RuntimeError(f"Environment variable {k} is note set")

    prompt = input("Prompt: ")
    chain = search_prompt(prompt)

    if not chain:
        print("Não foi possível iniciar o chat. Verifique os erros de inicialização.")
    else:
        print(chain)

if __name__ == "__main__":
    main()