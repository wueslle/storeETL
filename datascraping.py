from bs4 import BeautifulSoup as bs4
import requests as re
import re as regex

def get_notebook_data(url='https://lista.mercadolivre.com.br/notebook#D[A:notebook]'):
    response = re.get(url)
    notebooks = []

    if response.status_code == 200:
        soup = bs4(response.content, 'html.parser') 


        titulos = soup.find_all('a', class_='ui-search-link__title-card ui-search-link')
        precos = soup.find_all('span', class_='andes-money-amount__fraction')

    
        for titulo, preco in zip(titulos, precos):
            full_title = titulo.get_text().strip()
            
          
            match = regex.match(r'^(Notebook.*?(?:Core\s\w+\s\d+\w*))\s(.*)', full_title)
            if match:
                notebook = {
                    "name": match.group(1), 
                    "specs": match.group(2),  
                    "price": preco.get_text().strip().replace('.', '').replace(',', '.'),
                    "store":'Mercado Livre'
                }
                notebooks.append(notebook)
        print(notebooks)
        return notebooks
    else:
        print(f"Failed to retrieve data. Status code: {response.status_code}")
        return []
