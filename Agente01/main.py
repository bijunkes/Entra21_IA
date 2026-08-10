import requests
import re
from pysentimiento import create_analyzer

import os
from dotenv import load_dotenv

load_dotenv() 
access_token = os.getenv("ACCESS_TOKEN")

LANGUAGE = "pt"

class MercadoLivreAgent:
    
    def __init__(self, lang=LANGUAGE):
        self.analyzer = create_analyzer("sentiment", lang=lang)

    def extract_item_id(self, url):
        match = re.search(r'(MLB\d+)', url.replace('-', ''))
        return match.group(0) if match else None
    
    def fetch_reviews(self, item_id):
        url = f'https://api.mercadolibre.com/reviews/item/{item_id}?limit=30'
        headers = {"Authorization": f"Bearer {access_token}"}
        
        response = requests.get(url, headers=headers)
        
        print("Status:", response.status_code)
        print("Resposta:", response.text)
        
        if response.status_code == 200:
            return response.json().get("reviews", [])
        
        if response.status_code != 200:
            print(f"Item with ID {item_id} not found.")
            return []
        
    def analyze(self, url):
        item_id = self.extract_item_id(url)
        if not item_id:
            print("Invalid URL or item ID not found.")
            return
        
        reviews = self.fetch_reviews(item_id)
        
        if not reviews:
            print("No reviews found for this item.")
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
url = "https://www.mercadolivre.com.br/impressora-multifuncional-hp-deskjet-ink-advantage-2975-colorida-1-usb-20-de-alta-velocidade-wi-fi-de-banda-dupla-100-a-240-vca-aj4y4aak4/p/MLB62998911"
agente.analyze(url)