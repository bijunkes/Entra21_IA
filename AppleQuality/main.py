import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, ConfusionMatrixDisplay
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier


# Lendo base de dados
df = pd.read_csv('apple_quality.csv')


# Tratamento
df.drop(4000, inplace=True)
df.drop('A_id', axis=1, inplace=True)
df['Acidity'] = df['Acidity'].astype('float')


# Treino e Teste
X = df.drop('Quality', axis=1).values
y = df["Quality"].astype(str).to_numpy()

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, random_state=42)

modelos = {
    'Naive Bayes': GaussianNB(),
    'KNN': KNeighborsClassifier(n_neighbors=5),
    'Árvore de Decisão': DecisionTreeClassifier(random_state=42),
    'Forest': RandomForestClassifier(n_estimators=100, random_state=42)
}

predicts = {}

for nome, modelo in modelos.items():
  modelo.fit(X_train, y_train)
  previsao = modelo.predict(X_test)
  predicts[nome] = accuracy_score(y_test, previsao)
  
  
# Página
st.set_page_config(layout='wide')

col1, col2 = st.columns([0.3, 0.7])

with col1:
    st.title("Apple Quality")
    size = st.number_input("Size")
    weight = st.number_input("Weight")
    sweetness = st.number_input("Sweetness")
    crunchiness = st.number_input("Crunchiness")
    juiciness = st.number_input("Juiciness")
    ripeness = st.number_input("Ripeness")
    acidity = st.number_input("Acidity")
    
    prever = st.button("Classificar", use_container_width=True)
    
with col2:
    st.title("Accuracy")
    
    if prever:
        teste = np.array([[
            size,
            weight,
            sweetness,
            crunchiness,
            juiciness,
            ripeness,
            acidity
        ]])
    
        col_a, col_b = st.columns(2)
        col_c, col_d = st.columns(2)

        colunas = [col_a, col_b, col_c, col_d]

        for (nome, modelo), coluna in zip(modelos.items(), colunas):
            resultado = modelo.predict(teste)[0]
            predict = predicts[nome]
            
            previsao = modelo.predict(X_test)

            fig, ax = plt.subplots(figsize=(4, 4))

            ConfusionMatrixDisplay.from_predictions(
                y_test,
                previsao,
                ax=ax,
            )

            ax.set_title(nome)

            with coluna:
                with st.container(border=True):
                    st.subheader(nome)
                    st.metric("Accuracy", f"{predict:.2%}")

                    if resultado == "good":
                        st.success("Good")
                    else:
                        st.error("Bad")
                        
                    st.pyplot(fig)