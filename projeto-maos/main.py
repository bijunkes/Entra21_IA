import cv2
import numpy as np
import tensorflow as tf
from tensorflow.keras.layers import DepthwiseConv2D as OriginalDepthwiseConv2D

class CustomDepthwiseConv2D(OriginalDepthwiseConv2D):
    def __init__(self, *args, **kwargs):
        kwargs.pop("groups", None)
        super().__init__(*args, **kwargs)
        
model = tf.keras.models.load_model(
    "keras_model.h5",
    compile=False,
    custom_objects={
        "DepthwiseConv2D": CustomDepthwiseConv2D
    }
)
print("Modelo carregado com sucesso.")

with open("labels.txt", "r", encoding="utf-8") as arquivo:
    class_names = [linha.strip() for linha in arquivo.readlines()]
    
camera = cv2.VideoCapture(0)
if not camera.isOpened():
    print("Erro ao abrir a câmera")
    exit()
    
while True:
    ret, frame = camera.read()
    if not ret:
        print("Erro")
        break
    
    imagem = cv2.resize(frame, (224, 224))
    imagem = cv2.cvtColor(imagem, cv2.COLOR_BGR2RGB)
    imagem = np.asarray(imagem, dtype=np.float32)
    
    imagem = (imagem / 127.5) - 1
    
    entrada = np.expand_dims(imagem, axis=0)
    
    previsao = model.predict(entrada, verbose=0)
    indice = np.argmax(previsao[0])
    confianca = previsao[0][indice]
    classe = class_names[indice]
    
    texto = f"{classe}: {confianca * 100:.1f}%"
    cv2.putText(frame, texto, (20, 50),
        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2           
    )
    
    cv2.imshow(
        "Teachable Machine + OpenCV",
        frame
    )
    
    tecla = cv2.waitKey(1) & 0xFF
    if tecla == 27:
        break
    
camera.release()
cv2.destroyAllWindows()