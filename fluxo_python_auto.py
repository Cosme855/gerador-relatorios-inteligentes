import os
from dotenv import load_dotenv
from google import genai
import pandas as pd

# 1. Carregar a chave do ficheiro .env com segurança
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError(
        "A chave GEMINI_API_KEY não foi encontrada! "
        "Verifique se o ficheiro .env foi criado corretamente."
    )

# Configurar o cliente oficial do Gemini com a chave segura
client = genai.Client(api_key=api_key)

# 2. Parte de Dados: Simulando os números brutos calculados pelo Pandas
dados_mercado = {
    "faturamento_total_mes": "R$ 150.000",
    "variacao_faturamento": "-15% em relação ao mês anterior",
    "produto_com_maior_queda": "Produto X (queda de 35 nas vendas)",
    "categoria_mais_forte": "Categoria B (crescimento de 5%)",
}

# 3. Parte de IA: Criando o prompt com os dados brutos
prompt = f"""
Atue como um Consultor de Negócios Sênior. Analise os seguintes dados de desempenho da empresa:
- Faturamento Total: {dados_mercado['faturamento_total_mes']}
- Variação do Faturamento: {dados_mercado['variacao_faturamento']}
- Ponto Crítico: {dados_mercado['produto_com_maior_queda']}
- Ponto Positivo: {dados_mercado['categoria_mais_forte']}

Com base nesses dados, escreva um parágrafo executivo explicando os motivos potenciais para essa queda e sugira 2 ações estratégicas imediatas para a diretoria reverter o cenário do Produto X.
"""

# 4. Enviando para o Gemini
response = client.models.generate_content(
    model="gemini-3.8-flash",
    contents=prompt,
)

print("--- RELATÓRIO INTELIGENTE GERADO ---")
print(response.text)