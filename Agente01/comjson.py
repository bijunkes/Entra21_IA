import requests
import re
from pysentimiento import create_analyzer
import json

import os
from dotenv import load_dotenv

load_dotenv() 
access_token = os.getenv("ACCESS_TOKEN")

LANGUAGE = "pt"

class MercadoLivreAgent:
    
    def __init__(self, lang=LANGUAGE):
        self.analyzer = create_analyzer("sentiment", lang=lang)
           
    
    def fetch_reviews(self, source):
        if isinstance(source, dict):
            data = source
            
        elif isinstance(source, list):
            return source
        
        elif isinstance(source, str):
            if source.strip().endswith(".json"):
                with open(source, "r", encoding="utf-8") as f:
                    data = json.load(f)
            else:
                data = json.loads(source)
                
        else:
            raise ValueError("Formato de entrada não suportado.")

        if isinstance(data, dict):
            return data.get("reviews", [])
        
        return data
        
    def analyze(self, source):
        reviews = self.fetch_reviews(source)
        
        if not reviews:
            print("Nenhuma review encontrada.")
            return
        
        sentiments = {
            "POS": 0,
            "NEU": 0,
            "NEG": 0
        }
        
        for review in reviews:
            res = self.analyzer.predict(review["text"])
            resultado = res.output # POS, NEU, NEG
            sentiments[resultado] += 1
            
        total = len(reviews)
        pos_ratio = sentiments["POS"] / total
        
        if pos_ratio > 0.7:
            print("O produto é bem avaliado.")
        elif pos_ratio < 0.3:
            print("O produto é mal avaliado.")
        else:
            print("O produto tem avaliações mista.")
            
            
agente = MercadoLivreAgent()
json = ""
agente.analyze(json)