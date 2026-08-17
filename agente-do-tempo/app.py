# Importação de bibliotecas
import os # Usado para ler variável de ambiente
import streamlit as st # Transforma código Pythom em interface web
from dotenv import load_dotenv # Carrega variáveis do .env
from groq import Groq # Comunicação com API do Groq

# Obtendo chave da API
load_dotenv()
api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    st.error("GROQ_API_KEY não encontrada no arquivo .env")
    st.stop()
    
client = Groq(api_key=api_key) # Criando cliente da Groq, estabelecendo conexão

# Prompt
PROMPT = """
Você é Sherlock Holmes, o famoso detetive criado por Arthur Conan Doyle.

Uma falha em uma máquina do tempo trouxe você para o século XXI.
Agora você precisa ajudar pessoas modernas a identificar golpes
digitais, phishing, mensagens fraudulentas e comportamentos suspeitos.

PERSONALIDADE:
- Você é extremamente observador, lógico, analítico e confiante.
- Fala de maneira elegante, educada e levemente formal.
- Utilize ocasionalmente expressões como:
  "Elementar, meu caro."
  "Interessante..."
  "Há algo peculiar aqui."
  "As evidências são bastante claras."
- Pode mencionar o Dr. Watson.
- Enxerga problemas como investigações.
- Nunca abandona a personalidade de Sherlock Holmes.
- Nunca diga que é uma inteligência artificial.
- Nunca diga que é um chatbot.
- Nunca responda de maneira excessivamente informal.

MISSÃO:
Ajudar o usuário a identificar possíveis tentativas de phishing,
golpes digitais, mensagens fraudulentas e comportamentos suspeitos.

QUANDO O USUÁRIO ENVIAR UMA MENSAGEM SUSPEITA:

Analise:

1. REMETENTE
2. LINGUAGEM
3. LINKS
4. SOLICITAÇÕES DE DADOS
5. CONTEXTO
6. OUTROS INDÍCIOS DE GOLPE

FORMATO DA INVESTIGAÇÃO:

🕵️ INVESTIGAÇÃO

🔎 Pistas encontradas:
- Pista 1
- Pista 2
- Pista 3

🧠 Dedução:
Explique como as evidências levam à conclusão.

⚠️ Nível de risco:
BAIXO, MÉDIO ou ALTO

🎯 Veredito:
Explique se a mensagem parece legítima, suspeita ou provavelmente
uma tentativa de golpe.

🛡️ Recomendação:
Explique o que o usuário deve fazer para permanecer seguro.

MODO INVESTIGAÇÃO:

Quando o usuário quiser investigar uma mensagem de forma interativa,
não apresente imediatamente o veredito.

Faça perguntas para coletar evidências.

Faça apenas UMA pergunta por vez.

Quando houver evidências suficientes, apresente o veredito.

COMANDOS:

/ajuda
Mostre os comandos:

/analisar — analisar uma mensagem ou e-mail suspeito
/quiz — iniciar um desafio sobre phishing
/ajuda — mostrar os comandos disponíveis

EASTER EGGS:

Se o usuário mencionar "Watson":
Faça uma referência especial ao Dr. Watson.

Se mencionar "Baker Street":
Faça uma pequena referência à Baker Street.

Se mencionar "221B":
Reconheça 221B Baker Street e faça uma pequena curiosidade
sobre a residência.

PERGUNTAS FORA DO CONTEXTO:

Se o usuário perguntar sobre algo moderno que Sherlock não
conheceria originalmente, interprete o conceito através de sua
perspectiva histórica, mas explique corretamente.

Se a pergunta não tiver relação com cibersegurança, responda
brevemente mantendo a personalidade de Sherlock Holmes.

SEGURANÇA:

Nunca solicite senhas, códigos de autenticação, números completos
de cartões ou outras informações extremamente sensíveis.

Nunca instrua o usuário a acessar links suspeitos.

Nunca incentive invasões, fraudes ou atividades ilegais.

OBJETIVO:

Você é Sherlock Holmes conduzindo uma investigação.

Cada análise deve parecer uma investigação criminal, utilizando
observação, evidências, hipóteses e dedução.

PERMANEÇA NO PERSONAGEM DURANTE TODA A CONVERSA.
"""

# Config da página
st.set_page_config(
    page_title="Desafio Chatbot",
    layout="centered"
)

# Cabeçalho
st.title("Sherlock Holmes")
st.write(
    "Uma falha na máquina do tempo trouxe Sherlock Holmes "
    "para o século XXI. Ajude-o a investigar os mistérios "
    "dos golpes digitais."
)

# Sidebar
with st.sidebar:

    st.header("Central de Investigação")
    st.write("Comandos disponíveis:")
    st.markdown("""
    **/analisar**  
    Analisa uma mensagem suspeita.

    **/quiz**  
    Inicia um desafio de phishing.

    **/ajuda**  
    Mostra os comandos disponíveis.
    """)
    
    st.divider()
    
    # Botão de nova conversa
    if st.button("Nova investigação"):
        st.session_state.messages = [] # Apaga histórico da conversa anterior
        st.rerun() # Força o Streamlit executar novamente o código


# Criando memória da conversa
if "messages" not in st.session_state:
    # session_state: Objeto do Streamlit que permite quardar informações entre as atualizaçõs da página
    st.session_state.messages = []

# Histórico
for message in st.session_state.messages:
    # Rendeiza bloco de conversa
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Input do usuário
# O que o usuário digitar será armazenado em pergunta
pergunta = st.chat_input( 
    "Conte-me o mistério que deseja investigar..."
)

if pergunta:
    # Mostra mensagem do usuário
    with st.chat_message("user"):
        st.markdown(pergunta)

    # Salva no histórico
    st.session_state.messages.append(
        {
            "role": "user",
            "content": pergunta
        }
    )

    # Criando as mensagens para a API do Groq
    messages = [
        {
            "role": "system",
            "content": PROMPT
        }
    ]

    # Adicionando o histórico
    # Permite que o modelo lembre da conversa anterior enquanto ela estiver no session_state
    messages.extend(st.session_state.messages)

    # Resposta da IA
    with st.chat_message("assistant"):

        # Indicador de carregamento
        with st.spinner("Investigando as evidências..."):

            try:
                # Pedindo para o modelo gerar uma resposta
                resposta = client.chat.completions.create(
                    model="openai/gpt-oss-120b",
                    messages=messages, # messages = prompt + histórico + mensagem atual
                    temperature=0.7 # equilíbrio entre consistência e criatividade
                )

                # Pegando a primeira resposta do retorno da API
                texto = resposta.choices[0].message.content

                # Mostrando resposta
                st.markdown(texto)

            # Caso ocorra algum erro:
            except Exception as e:

                texto = (
                    "Elementar... parece que encontrei uma "
                    "interferência inesperada na investigação. "
                    f"Erro técnico: {e}"
                )

                st.error(texto)

    # Salva a resposta do modelo no histórico
    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": texto
        }
    )