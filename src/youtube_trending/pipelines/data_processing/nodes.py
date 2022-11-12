import json
import os
import pandas as pd
import numpy as np
import logging
from pandas import DataFrame
from typing import Dict

log = logging.getLogger(__name__)

def read_files(datasets_path: str):
    '''Sczytuje csv'ki i JSONy zawierające informacje
    o kategoriach ze ścieżki z danymi
    
    Wejśćie: 
    datasets_path: string będący ścieżką do danych

    Wyjście:
    csvs: słownik gdzie kluczem jest nazwa pliku, a wartością dataframe
    categories: słownik gdzie kluczem jest id kategorii, a wartością nazwa
    '''
    
    csvs = {}
    categories = {}

    for f in os.listdir(datasets_path):
        file_path = datasets_path + "/" + f
        if f.endswith('.json'):
            with open(file_path, 'r') as file:
                # otwarty plik ładujemy jako json
                zbigniew = json.load(file)
                # wybieramy listę items
                items = zbigniew["items"]
                for item in items:
                    # przechodzimy po itemach, wyszukując id kategorii oraz nazwę
                    categories[int(item['id'])] = item['snippet']['title']
                    
        elif f.endswith('.csv'):
            csv = pd.read_csv(file_path, encoding='ISO-8859-1')
            # Dodaje do słownika
            csvs[f] = csv
    
    return csvs, categories











# {1: "Film & Animations", 10: "Music"}

def prepare_trending_data(csvs: Dict[str, DataFrame], categories: Dict[int, str]):
    '''
    '''
    trending_data = {}

    for country, csv in csvs.items():
        # wzięte z artykułu
        csv["description"] = csv["description"].fillna(value="")

        # brzydki sposób na zamianę id kategorii na jej nazwę
        csv["category"] = ""
        for row in csv.index:
            csv["category"][row] = categories[int(csv["category_id"][row])]
            
        csv.pop("category_id")
        trending_data[country] = csv

    return trending_data