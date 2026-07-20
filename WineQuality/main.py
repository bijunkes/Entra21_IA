import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
import xgboost as xgb

from sklearn.metrics import accuracy_score, ConfusionMatrixDisplay
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

# Lendo base de dados
df_tinto = pd.read_csv('winequality-red.csv', sep=';')
df_tinto['tipo'] = 'tinto'

df_branco = pd.read_csv('winequality-white.csv', sep=';')
df_branco['tipo'] = 'branco'

df = pd.concat([df_tinto, df_branco], ignore_index=True)

# Treino e teste
le = LabelEncoder()

X = df.drop('tipo', axis=1).values
y = le.fit_transform(df['tipo'].values)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42
)

modelos = {
    'Naive Bayes': GaussianNB(),
    'KNN': KNeighborsClassifier(n_neighbors=5),
    'Decision Tree': DecisionTreeClassifier(random_state=42),
    'Forest': RandomForestClassifier(n_estimators=100, random_state=42),
    'SVC':  SVC(kernel='rbf', random_state=42),
    'Log. Regression': LogisticRegression(max_iter=1000, random_state=42),
    'Xgboost': xgb.XGBClassifier(random_state=42)
}

predicts = {}

for nome, modelo in modelos.items():
    modelo.fit(X_train, y_train)
    previsao = modelo.predict(X_test)
    predicts[nome] = accuracy_score(y_test, previsao)

# Página
st.set_page_config(layout='wide')

st.title("Classificação de Vinhos")

col1, col2 = st.columns([0.2, 0.8])

with col1:
    st.header("Atributos")
    fixed_acidity = st.number_input("fixed acidity")
    volatile_acidity = st.number_input("volatile acidity")
    citric_acid = st.number_input("citric acid")
    residual_sugar = st.number_input("residual sugar")
    chlorides = st.number_input("chlorides")
    free_sulfur_dioxide = st.number_input("free sulfur dioxide")
    total_sulfur_dioxide = st.number_input("total sulfur dioxide")
    density = st.number_input("density")
    pH = st.number_input("pH")
    sulphates = st.number_input("sulphates")
    alcohol = st.number_input("alcohol")
    quality = st.number_input("quality")
    
    prever = st.button("Classificar", use_container_width=True)
    
with col2:
    st.header("Precisão")
    
    if prever:
        teste = np.array([[
            fixed_acidity,
            fixed_acidity,
            citric_acid,
            residual_sugar,
            chlorides,
            free_sulfur_dioxide,
            total_sulfur_dioxide,
            density,
            pH,
            sulphates,
            alcohol,
            quality
        ]])
    
        linha1 = st.columns(4)
        linha2 = st.columns(4)
        linha3 = st.columns(4)

        colunas = linha1 + linha2 + linha3

        for (nome, modelo), coluna in zip(modelos.items(), colunas):
            resultado = modelo.predict(teste)[0]
            resultado = le.inverse_transform([resultado])[0]
            
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
                    st.metric("Precisão", f"{predict:.2%}")

                    if resultado == "tinto":
                        st.error("Tinto")
                    else:
                        st.info("Branco")
                        
                    st.pyplot(fig)
    