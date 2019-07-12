import requests
from bs4 import BeautifulSoup

url = requests.get('https://www.google.com.br/imghp?hl=pt-BR&tab=wi')
soup = BeautifulSoup(url.text,'lxml')

'''----------------------------Extraindo Links------------------------------------'''

def extrair_links(content):   
    links = set()             # set() tipo uma lista porem faz um agregado de informação sem uma ordem

    for tag in soup.find_all('a', href=True):
        if tag['href'].startswith('http'):
            links.add(tag['href'])
            print(links)
    return links
          

    
   
links = extrair_links(url.text)