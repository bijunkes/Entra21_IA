import pymupdf
from gliner import GLiNER


# ==========================================
# CONFIGURAÇÕES
# ==========================================

file_path = r"C:\Users\aluno\Desktop\Entra21_IA\Teste\teste.pdf"


# ==========================================
# CARREGAR MODELO
# ==========================================

print("Carregando modelo GLiNER...")

model = GLiNER.from_pretrained(
    "gliner-community/gliner_small-v2.5"
)

print("Modelo carregado!")


# ==========================================
# PDF → TEXTO
# ==========================================

def extract_text_from_pdf(file_path):

    document = pymupdf.open(file_path)

    text = ""

    for page in document:
        text += page.get_text()

    document.close()

    return text


# ==========================================
# GLINER → ENTIDADES
# ==========================================

def extract_entities(text):

    labels = [
        "person",
        "job title",
        "skill",
        "education",
        "company",
        "location",
        "language",
        "project"
    ]

    entities = model.predict_entities(
        text,
        labels,
        threshold=0.35
    )

    return entities


# ==========================================
# EXECUÇÃO
# ==========================================

texto = extract_text_from_pdf(file_path)

print("\n================================")
print("          TEXTO DO PDF")
print("================================")

print(texto)


print("\n================================")
print("       ENTIDADES GLINER")
print("================================")

entities = extract_entities(texto)

for entity in entities:

    print(
        f"{entity['text']} "
        f"-> {entity['label']} "
        f"(score: {entity['score']:.2f})"
    )