import json
import os
import pandas as pd
import numpy as np

def read_files(datasets_path: str):
    '''Sczytuje csv'ki i JSONy zawierające informacje
    o kategoriach ze ścieżki z danymi
    
    Wejśćie: 
    datasets_path: string będący ścieżką do danych

    Wyjście:
    csvs: lista dataframe'ów z dodaną informacją o kraju pochodzenia
    categories: słownik gdzie kluczem jest id kategorii, a wartością nazwa
    '''
    
    csvs = []
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
            # Dodaje kolumnę country jako nazwę czytanego pliku
            csv["country"] = f
            # Usuwa tę kolumnę, żeby dodać ją jako pierwszą
            country_col = csv.pop("country")
            csv.insert(0, "country", country_col)
            # Dodaje do listy
            csvs.append(csv)
    
    return csvs, categories

