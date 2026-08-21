import json
import urllib.request

MODELO = "llama3.2:3b"
URL = "http://localhost:11434/api/chat"

def chamar_IA(mensagem, formato=None):
    corpo = {
        "model": MODELO,
        "messages": mensagem,
        "stream": False,
        "options": {"temperature": 0}
    }
    
    if formato is not None:
        corpo["format"] = formato

    requisicao = urllib.request.Request(
        URL,
        data=json.dumps(corpo).encode("utf-8"),
        headers={"Content-Type":"application/json"}
    )

    with urllib.request.urlopen(requisicao) as conexao:
        return json.loads(conexao.read())
    
#content = input("Faça uma pergunta: ")

#if content:
#    chamar_IA([
#        {"role": "user", "content": content}
#    ])
            
INSTRUCAO = """
Voce classifica avaliacoes de produtos em portugues do Brasil.

Responda com um JSON contendo:

- sentimento: "positivo", "neutro" ou "negativo"

- motivo: no maximo 10 palavras

Ironia conta como o sentimento real, nao o literal.
"""

ESQUEMA = {
    "type": "object",
    "properties": {
        "sentimento": {
            "type": "string",
            "enum": ["positivo", "neutro", "negativo"]
        },
        "motivo": {
            "type": "string"
        }
    },
    "required": ["sentimento", "motivo"]
}

def classificar(texto):
    mensagem = [
        {"role": "system", "content": INSTRUCAO},
        {"role": "user", "content": texto}
    ]
    formato = ESQUEMA
    saida = chamar_IA(mensagem, formato)
    
    # O Ollama retorna o texto gerado dentro de message["content"].
    # Como usamos o format ESQUEMA, esse conteúdo é uma string JSON que precisamos converter para dicionário.
    conteudo_str = saida["message"]["content"]
    return json.loads(conteudo_str)

VALOR = {"positivo": 1, "neutro": 0, "negativo": -1}

with open("avaliacoes.json", encoding="utf-8") as arquivo:
    dados = json.load(arquivo)
    
resultados = []

for avaliacao in dados["avaliacoes"]:
    analise = classificar(avaliacao["texto"])
    analise["id"] = avaliacao["id"]
    analise["nota"] = avaliacao["nota"]
    analise["texto"] = avaliacao["texto"]
    
    resultados.append(analise)
    print(
        f'Id {analise["id"]} - '
        f'Nota: {analise["nota"]} - '
        f'Sentimento: {analise["sentimento"]}'
    )
    
notas = [VALOR[r["sentimento"]] for r in resultados]

media = sum(notas) / len(notas)

positivas = notas.count(1)
neutras = notas.count(0)
negativas = notas.count(-1)

print()
print("Produto:", dados["produto"])
print(len(notas), " Avaliações")
print("Média de sentimento: %+.2f (escala -1 a +1)" % media)
print("Positivas: %d | Negativas: %d" % (positivas, negativas))
print("Qualidade percebida: %.1f / 10" % ((media + 1) * 5))