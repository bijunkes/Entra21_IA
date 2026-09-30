from flask import Flask, request, jsonify
import joblib

app = Flask(__name__)
modelo = joblib.load('modelo.joblib')

@app.route('/')
def index():
    return jsonify({'mensagem':'API funcionando'})

@app.route('/predict', methods=['POST'])
def predict():
    dados = request.json
    age = dados['age']
    loan = dados['loan']
    income = dados['income']
    entrada = [[age, income, loan]]
    previsao = modelo.predict(entrada)

    return jsonify({'previsao': int(previsao[0])})

if __name__=='__main__':
    app.run(host='0.0.0.0', port=5000)