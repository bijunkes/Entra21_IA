import json
import urllib.request

MODELO = "llama3.2:3b"
URL = "http://localhost:11434/api/chat"

def chamar_IA(mensagem):
    corpo = {
        "model": MODELO,
        "messages": mensagem,
        "stream": False,
        "options": {"temperature": 0}
    }

    requisicao = urllib.request.Request(
        URL,
        data=json.dumps(corpo).encode("utf-8"),
        headers={"Content-Type":"application/json"}
    )

    with urllib.request.urlopen(requisicao) as conexao:
        return json.loads(conexao.read())
    
content = input("Faça uma pergunta: ")

if content:
    chamar_IA([
        {"role": "user", "content": content}
    ])
            
INSTRUCAO = """
Voce classifica avaliacoes de produtos em portugues do Brasil.

Responda com um JSON contendo:

- sentimento: "positivo", "neutro" ou "negativo"

- resposta: responde a pergunta do prompt (se houver)

- motivo: no maximo 10 palavras

Ironia conta como o sentimento real, nao o literal.
"""

texto = "Chegou rapido, mas o lado direito veio mudo."

mensagem = [
    {"role": "system", "content": INSTRUCAO},
    {"role": "user", "content": content}
]

saida = chamar_IA(mensagem)
print(saida)