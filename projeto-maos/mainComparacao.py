import cv2
import numpy as np
import tensorflow as tf
import streamlit as st

from PIL import Image
from tensorflow.keras.layers import DepthwiseConv2D as OriginalDepthwiseConv2D

class CustomDepthwiseConv2D(OriginalDepthwiseConv2D):
    def __init__(self, *args, **kwargs):
        kwargs.pop("groups", None)
        super().__init__(*args, **kwargs)

model = tf.keras.models.load_model(
    "keras_comp.h5",
    compile=False,
    custom_objects={
        "DepthwiseConv2D": CustomDepthwiseConv2D
    }
)

print("Modelo carregado com sucesso.")

with open("labels_comp.txt", "r", encoding="utf-8") as arquivo:
    class_names = [linha.strip() for linha in arquivo.readlines()]

st.title("Identificador de Maçãs e Tomates")

st.write(
    "Envie uma ou várias imagens de maçãs ou tomates."
)

arquivos = st.file_uploader(
    "Escolha as imagens",
    type=["jpg", "jpeg", "png"],
    accept_multiple_files=True
)

if arquivos:

    st.write(f"{len(arquivos)} imagem(ns) selecionada(s).")

    for arquivo in arquivos:

        imagem = Image.open(arquivo).convert("RGB")

        st.image(
            imagem,
            caption=arquivo.name,
            use_container_width=True
        )


    if st.button("Identificar todas"):

        st.subheader("Resultados")

        for arquivo in arquivos:

            imagem = Image.open(arquivo).convert("RGB")

            imagem = np.array(imagem)

            imagem = cv2.resize(
                imagem,
                (224, 224)
            )

            imagem = np.asarray(
                imagem,
                dtype=np.float32
            )

            imagem = (imagem / 127.5) - 1

            entrada = np.expand_dims(
                imagem,
                axis=0
            )

            previsao = model.predict(
                entrada,
                verbose=0
            )[0]

            indice = np.argmax(previsao)

            classe = class_names[indice]

            confianca = previsao[indice]

            st.markdown("---")

            st.subheader(
                f"{arquivo.name}"
            )

            st.success(
                f"Resultado: {classe}"
            )

            st.write("Probabilidade:")

            for i, nome_classe in enumerate(class_names):

                probabilidade = float(previsao[i])

                st.write(
                    f"{nome_classe}: "
                    f"{probabilidade * 100:.1f}%"
                )

                st.progress(
                    min(probabilidade, 1.0)
                )
