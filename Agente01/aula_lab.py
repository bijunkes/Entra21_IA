#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
==========================================================================
 LABORATÓRIO DE NLP COM PYSENTIMIENTO
 Análise de sentimento, emoção, ironia e discurso de ódio em PT-BR
==========================================================================
 
 COMO USAR
 ---------
 Google Colab:
     !pip install -q pysentimiento
     (envie este arquivo e rode)  %run aula_lab.py
 
 Terminal:
     pip install pysentimiento
     python aula_lab.py            -> menu interativo
     python aula_lab.py --demo 3   -> roda direto o módulo 3
 
 OBSERVAÇÃO: na primeira execução os modelos são baixados do HuggingFace
 (~500 MB por tarefa). Rode o módulo 1 antes da aula para aquecer o cache.
 
 MÓDULOS
 -------
 1. Normalização: o que o modelo realmente lê
 2. Raio-X multitarefa: 4 modelos sobre a mesma frase
 3. Léxico x Transformer: por que bag-of-words não entende negação
 4. Explicabilidade: qual palavra decidiu o resultado?
 5. Triagem em lote: aplicação real
 6. Modo livre: o aluno digita o próprio texto
 7. Desafio: engane o modelo
==========================================================================
"""
 
import math
import sys
 
# ------------------------------------------------------------------ #
# 0. INFRAESTRUTURA                                                    #
# ------------------------------------------------------------------ #
 
IDIOMA = "pt"          # "pt", "es", "en", "it"
USAR_COR = True        # desligue se o terminal não renderizar ANSI
 
 
class C:
    """Códigos ANSI para deixar a saída legível no projetor."""
    RESET = "\033[0m" if USAR_COR else ""
    NEG = "\033[1m" if USAR_COR else ""
    DIM = "\033[2m" if USAR_COR else ""
    VERDE = "\033[92m" if USAR_COR else ""
    VERM = "\033[91m" if USAR_COR else ""
    AMAR = "\033[93m" if USAR_COR else ""
    AZUL = "\033[96m" if USAR_COR else ""
    ROXO = "\033[95m" if USAR_COR else ""
 
 
def instalar_dependencias():
    """Instala o pysentimiento se ele ainda não estiver disponível."""
    try:
        import pysentimiento  # noqa: F401
        return True
    except ImportError:
        print(f"{C.AMAR}pysentimiento não encontrado. Instalando...{C.RESET}")
        import subprocess
        subprocess.check_call(
            [sys.executable, "-m", "pip", "install", "-q", "pysentimiento"]
        )
        print(f"{C.VERDE}Instalado. Se estiver no Colab e der erro de import, "
              f"reinicie o runtime e rode de novo.{C.RESET}")
        return True
 
 
def titulo(texto):
    linha = "═" * (len(texto) + 2)
    print(f"\n{C.AZUL}╔{linha}╗")
    print(f"║ {C.NEG}{texto}{C.RESET}{C.AZUL} ║")
    print(f"╚{linha}╝{C.RESET}")
 
 
def barra(valor, largura=28):
    """Barra de progresso em ASCII para uma probabilidade entre 0 e 1."""
    valor = max(0.0, min(1.0, float(valor)))
    n = int(round(valor * largura))
    return "█" * n + "░" * (largura - n)
 
 
def cor_rotulo(rotulo):
    r = str(rotulo).upper()
    if r in ("POS", "JOY", "SURPRISE"):
        return C.VERDE
    if r in ("NEG", "ANGER", "SADNESS", "FEAR", "DISGUST", "HATEFUL",
             "AGGRESSIVE", "TARGETED", "IRONIC"):
        return C.VERM
    return C.AMAR
 
 
def confianca(probas):
    """
    Confiança = 1 - entropia normalizada.
    1.0 = o modelo cravou uma classe.  0.0 = ele está em cima do muro.
    Serve para ensinar que classificador devolve DISTRIBUIÇÃO, não verdade.
    """
    p = [max(1e-12, float(v)) for v in probas.values()]
    total = sum(p)
    p = [x / total for x in p]
    k = len(p)
    if k < 2:
        return 1.0
    h = -sum(x * math.log(x) for x in p)
    return 1.0 - h / math.log(k)
 
 
# ------------------------------------------------------------------ #
# 1. CACHE DE ANALISADORES (carrega sob demanda)                      #
# ------------------------------------------------------------------ #
 
_CACHE = {}
_INDISPONIVEIS = set()
 
TAREFAS = {
    "sentiment": "Sentimento",
    "emotion": "Emoção",
    "hate_speech": "Discurso de ódio",
    "irony": "Ironia",
}
 
 
def get_analyzer(tarefa, lang=IDIOMA, silencioso=False):
    """
    Devolve o analisador da tarefa ou None se o par tarefa/idioma
    não tiver modelo publicado. Nem toda tarefa existe em todo idioma.
    """
    chave = (tarefa, lang)
    if chave in _CACHE:
        return _CACHE[chave]
    if chave in _INDISPONIVEIS:
        return None
 
    from pysentimiento import create_analyzer
    try:
        if not silencioso:
            print(f"{C.DIM}   carregando modelo de "
                  f"{TAREFAS.get(tarefa, tarefa)} [{lang}]...{C.RESET}")
        analyzer = create_analyzer(task=tarefa, lang=lang)
        _CACHE[chave] = analyzer
        return analyzer
    except Exception as e:
        _INDISPONIVEIS.add(chave)
        if not silencioso:
            print(f"{C.AMAR}   [indisponível] {tarefa}/{lang}: "
                  f"{type(e).__name__}{C.RESET}")
        return None
 
 
def formatar_saida(res):
    """A saída de tarefas multirrótulo (ódio) vem como lista, não string."""
    saida = res.output
    if isinstance(saida, (list, tuple, set)):
        return ", ".join(saida) if saida else "nenhum"
    return str(saida)
 
 
def multirrotulo(res):
    return isinstance(res.output, (list, tuple, set))
 
 
# ------------------------------------------------------------------ #
# CORPUS DE AULA                                                       #
# ------------------------------------------------------------------ #
 
# Frases escolhidas para QUEBRAR abordagens ingênuas.
# O terceiro campo é o rótulo de referência (discutível de propósito:
# use isso para falar de divergência entre anotadores).
ARMADILHAS = [
    ("Adorei o produto, chegou antes do prazo!",            "POS", "fácil"),
    ("Não gostei nada do atendimento.",                     "NEG", "negação"),
    ("Nada mal, viu? Bem melhor do que eu esperava.",        "POS", "negação dupla"),
    ("Que ótimo, o voo atrasou cinco horas e ninguém avisou.", "NEG", "ironia"),
    ("O celular é bom, mas a bateria é horrível.",           "NEG", "sentimento misto"),
    ("Produto entregue conforme descrito na embalagem.",     "NEU", "sem polaridade"),
    ("Não é ruim.",                                          "POS", "negação dupla"),
    ("Melhor compra que já fiz na vida! 🥰",                  "POS", "emoji"),
    ("Estou impressionado com a capacidade dessa empresa de piorar.", "NEG", "sarcasmo"),
    ("Amei esperar três horas na fila 🙃",                    "NEG", "ironia + emoji"),
    ("O produto é exatamente o que eu esperava.",            "NEU", "ambíguo"),
    ("kkkkk esse filme é tão ruim que fica bom",             "POS", "gíria + inversão"),
]
 
# Comentários fictícios para a triagem em lote (módulo 5).
CAIXA_DE_ENTRADA = [
    "Alguém sabe se a aula de quinta foi remarcada?",
    "Esse sistema é uma porcaria, perdi meu trabalho inteiro de novo!!!",
    "Muito obrigado pelo material, salvou minha prova 🙏",
    "não consigo fazer login desde ontem, já tentei de tudo",
    "A plataforma caiu no meio da entrega e agora perdi o prazo. Inaceitável.",
    "Achei a explicação de polimorfismo bem clara, valeu!",
    "O boleto venceu e o acesso sumiu, mas paguei ontem",
    "vocês são uns incompetentes, ninguém responde nada",
    "Tudo certo por aqui, só passei pra agradecer",
    "Segue em anexo o print do erro que apareceu.",
    "Odeio esse curso, odeio esse professor, odeio tudo",
    "A interface nova ficou muito melhor que a anterior 👏",
]
 
# Léxico deliberadamente simples: representa a família bag-of-words.
LEXICO = {
    # positivos
    "adorei": 2, "amei": 2, "ótimo": 2, "otimo": 2, "bom": 1, "boa": 1,
    "melhor": 2, "excelente": 2, "gostei": 2, "maravilhoso": 2, "top": 1,
    "recomendo": 2, "perfeito": 2, "rápido": 1, "clara": 1, "obrigado": 1,
    # negativos
    "ruim": -2, "horrível": -3, "horrivel": -3, "péssimo": -3, "pessimo": -3,
    "odeio": -3, "detestei": -3, "atrasou": -2, "mal": -2, "piorar": -2,
    "porcaria": -3, "incompetentes": -3, "inaceitável": -3, "perdi": -1,
    "caiu": -1, "erro": -1,
}
 
 
def analise_lexical(texto):
    """Baseline clássico: soma pesos de palavras isoladas. Ignora contexto."""
    tokens = "".join(
        ch.lower() if (ch.isalnum() or ch.isspace()) else " " for ch in texto
    ).split()
    escore = sum(LEXICO.get(t, 0) for t in tokens)
    achados = [(t, LEXICO[t]) for t in tokens if t in LEXICO]
    if escore > 0:
        return "POS", escore, achados
    if escore < 0:
        return "NEG", escore, achados
    return "NEU", escore, achados


###
### Módulo 1: Normalização
###


def modulo1_normalizacao():
    """
    Módulo 1: Normalização
    ---------------------
    O que o modelo realmente lê? Vamos ver como a normalização afeta
    a entrada do modelo. A ideia é mostrar que o modelo não vê emojis,
    gírias, acentos, etc. Ele só vê tokens.
    """
    titulo("MÓDULO 1: NORMALIZAÇÃO")

    from pysentimiento.preprocessing import preprocess_tweet
## dontpad.com/nlp_11

    exemplos = [
        "@joaozinho vc viu isso??? https://exemplo.com/noticia #ForaBug 😡😡",
        "kkkkkkkkkkkkkk nao acreditooooo que isso aconteceu de novo",
        "MEU DEUS!!! que absurdo 🤬 chama o @suporte urgente",
        "amei demaisss o novo layout 😍😍😍 #ParabensEquipe",
    ]

    print("\nAntes de classifica, o texto passar por NORMALIZACAO")
    print("Comparar a entrada crua com o que chega no tokenizador")

    for texto in exemplos:
        normalizado = preprocess_tweet(texto, lang=IDIOMA)
        print(f"\n{C.NEG}Texto original:{C.RESET} {texto}")
        print(f"{C.NEG}Texto normalizado:{C.RESET} {normalizado}")


def raio_x(texto, mostrarTitulo= True):
    """
    Módulo 2: Raio-X multitarefa
    ---------------------------
    Mostra o resultado de 4 modelos sobre a mesma frase.
    """
    if mostrarTitulo:
        titulo(f"\n{C.NEG} \"{texto}\"{C.RESET}")

    for tarefa, nome in TAREFAS.items():
        analyzer = get_analyzer(tarefa)
        if analyzer is None:
            continue

        res = analyzer.predict(texto)
        rotulo = formatar_saida(res)
        cor = cor_rotulo(res.output if not multirrotulo(res) else rotulo)
        conf = confianca(res.probas)

        print(f"{C.AZUL}|{C.RESET}")
        print(f"{C.AZUL}|—— {C.RESET} {C.NEG} {nome:<18} {C.RESET}", end="")

        if not multirrotulo(res):
            conf = confianca(res.probas)
            marca = "cravou" if conf > 0.6 else ("em cima do muro" if conf < 0.25 else "razoável")
            print(f"{C.DIM} (confianca {conf:.0%} – {marca}){C.RESET}")
        else:
            print(f"{C.DIM} (multirrótulo: probabilidades independentes){C.RESET}")
        
        print(f"{C.AZUL}└{'─' * 50}{C.RESET}")

def modulo2_raio_x():
    """
    Módulo 2: Raio-X multitarefa
    ---------------------------
    Mostra o resultado de 4 modelos sobre a mesma frase.
    """
    titulo("MÓDULO 2: RAIO-X MULTITAREFA")

    for texto in [
        "Que ótimo, o voo atrasou cinco horas e ninguém avisou.",
        "Muito obrigado pelo material, salvou minha prova 🙏",
        "Alguém sabe se a aula de quinta foi remarcada?",
    ]:
        raio_x(texto)

modulo2_raio_x()


def modulo3_lexico_vs_transformer():
    """
    Módulo 3: Léxico x Transformer
    -----------------------------
    Por que bag-of-words não entende negação.
    """
    titulo("MÓDULO 3: LÉXICO X TRANSFORMER")

    analyzer = get_analyzer("sentiment")
    if analyzer is None:
        print(f"{C.AMAR}Modelo de sentimento não disponível para {IDIOMA}.{C.RESET}")
        return

    print("O léxico soma pesos de palavraas isoladas - ignora contexto")
    print("O transformer lê a frase inteira e entende negação, ironia, emojis, etc.\n")

    print(f"{C.NEG}{'FRASE':<48} {'REF':>4}{'LEXICO':>5} {'MODELO':>5} ARMADILHA{C.RESET}")
    print("–" * 96)

    acertos_lex = acertos_mod = 0
    textos = [t for t, _, _ in ARMADILHAS]
    resultados = analyzer.predict(textos)

    for(texto, ref, tipo), res in zip(ARMADILHAS, resultados):
        lex, escore, achados = analise_lexical(texto)
        mod = res.output

        ok_lex = lex == ref
        ok_mod = mod == ref
        acertos_lex += ok_lex
        acertos_mod += ok_mod

        recorte = texto if len(texto) <= 46 else texto[:43] + "..."
        m_lex = f"{C.VERDE}✓{C.RESET}" if ok_lex else f"{C.VERM}✗{C.RESET}"
        m_mod = f"{C.VERDE}✓{C.RESET}" if ok_mod else f"{C.VERM}✗{C.RESET}"

        print(f"{recorte:<48} {ref:>4} {lex:>5} {m_lex} {mod:>5} {m_mod} {C.DIM}{tipo}{C.RESET}")

    n = len(ARMADILHAS)
    print("–"*96)
    print(f"Acertos léxico: {acertos_lex}/{n}")
    print(f"Acertos transformer: {acertos_mod}/{n}")

modulo3_lexico_vs_transformer()
