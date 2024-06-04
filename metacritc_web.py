import os
import re
import time
import math
import requests
import pandas as pd
from bs4 import BeautifulSoup

os.system('cls')

destino = 'Sua pasta de destino'
headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"}

dic_games = {'Nome':[],'Ano':[],'Nota':[]}

def Total_itens():
    url_page = 'https://www.metacritic.com/browse/game/pc/all/all-time/metascore/?releaseYearMin=1958&releaseYearMax=2024&platform=pc&page=1'
    site = requests.get(url_page, headers=headers)
    soup = BeautifulSoup(site.content, 'html.parser')
    itens = soup.find('span', class_=re.compile('c-finderControls_total'))
    data_total = itens.text.split(" ")
    total = data_total[0].replace(",","")
    qtd = math.ceil((int(total)/24))
    return qtd

def Games_meta(dic):
    
    ultima_pag = Total_itens()
    print(f"Inicializando Programa. Paginas = {ultima_pag}")  

    for i in range(1,ultima_pag+1):
        
        url_page = f'https://www.metacritic.com/browse/game/pc/all/all-time/metascore/?releaseYearMin=1958&releaseYearMax=2024&platform=pc&page={i}'
        site = requests.get(url_page, headers=headers)
        soup = BeautifulSoup(site.content, 'html.parser')
        games = soup.find_all('div', class_=re.compile('c-finderProductCard_info'))
        time.sleep(5)
        
        for game in games:
            try:
                data_title = game.find('div', class_=re.compile('c-finderProductCard_title'))
                nome = data_title.find('span').find_next_sibling('span').text

            except Exception as erro:
                print(erro)
            
            try:
                ano_data = game.find('div', class_='c-finderProductCard_meta')
                ano = ano_data.find('span').text.split()
                ano_final = ano[0] + ' ' + ano[1] + ' ' + ano[2]
                        
            except Exception as erro:
                continue
            
            try:
                nota_data = game.find('div', class_=re.compile('c-siteReviewScore_background'))
                nota = nota_data.find('span').text
                
            except Exception as erro:
                continue  

            dic['Nome'].append(nome)
            dic['Ano'].append(ano_final)
            dic['Nota'].append(nota)

            print(f'Nome: {nome} Ano: {ano_final} Nota: {nota}')
        
        i += 1
        print(f'Fim da pagina {i-1} de {ultima_pag}')

print('Inicio do Programa...')
Games_meta(dic_games)             

df = pd.DataFrame(dic_games)
df.to_csv(f'{destino}/Games_metacritc.csv', encoding='utf-8', sep=';')

print('Fim!')