# Gerador de Relatórios Inteligentes com Python e IA (Gemini)

Projeto desenvolvido para a plataforma DIO, integrando automação de dados com Inteligência Artificial para gerar diagnósticos executivos e ações estratégicas de negócios.

## 🚀 Tecnologias Utilizadas
- **Python 3.15**
- **Pandas** (Análise e estruturação de dados)
- **Google GenAI SDK** (Modelo Gemini 3.8 Flash)
- **Python-Dotenv** (Gestão segura de credenciais e chaves de API)

## 🔒 Segurança
A chave de API é gerenciada por meio de variáveis de ambiente com um arquivo `.env` (ignorado via `.gitignore`), garantindo a proteção das credenciais segundo as melhores práticas de desenvolvimento Open Source.

## ⚙️ Como Executar o Projeto

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/SEU_USUARIO/SEU_REPOSITORIO.git
   cd "projeto auto excel"

Instale as dependências:
pip install google-genai pandas python-dotenv

Configure a Chave de API:
Crie um arquivo .env na raiz do projeto contendo:

GEMINI_API_KEY=sua_chave_aqui

Execute o Script: 
python fluxo_python_auto.py