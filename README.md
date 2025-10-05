# Desafio MBA Engenharia de Software com IA - Full Cycle

1. **Criar e ativar um ambiente virtual (`venv`):**

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # No Windows: venv\Scripts\activate
   ```

2. **Instalar as dependências:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Configurar as variáveis de ambiente:**

   - Duplique o arquivo `.env.example` e renomeie para `.env`
   - Abra o arquivo `.env` e substitua os valores pelas suas chaves de API reais, pelos modelos de embedding e LLM que pretende utilizar e pelo caminho do PDF no sistema de arquivos.

3. **Iniciar container Docker:**

   Executar o seguinte comando no terminal para criar/iniciar o container Docker:

   ```bash
   docker compose up -d
   ```

4. **Realizar a ingestão do arquivo PDF no banco de dados:**

   Acesse a raiz do projeto e execute o seguinte comando:

   ```bash
   python3 .\src\ingest.py
   ```

4. **Habilitar chat do modelo:**

   Execute o seguinte comando:

   ```bash
   python3 .\src\chat.py
   ```
   Esse script habilitará um prompt para que seja feita uma pergunta para o modelo. As perguntas devem ser feitas com base no conteúdo do PDF "document.pdf".

   Exemplos:
      - Qual o faturamento da empresa Alfa Turismo S. A.?
      - Quais empresas possuem um faturamento superior a R$ 100.000.000,00?

   Perguntas feitas fora do contexto do conteúdo existente no PDF não deverão ser respondidas.

   Para cada nova pergunta, executar o script chat.py novamente.