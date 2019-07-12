import requests
from bs4 import BeautifulSoup
import urllib.request
import sys


url = requests.get('https://www.python.org/')
soup = BeautifulSoup(url.text,'lxml')

'''----------------------------Extraindo Links------------------------------------'''

def extrair_links(content):   
    links = set()             # set() tipo uma lista porem faz um agregado de informação sem uma ordem

    for tag in soup.find_all('a', href=True):
        if tag['href'].startswith('http'):
            links.add(tag['href'])

    return links
   
links = extrair_links(url.text)


for index, value in enumerate(links):
    if value in links:
        with(open('/home/rafael/Projetos_Python/Projetos_Online/Arquivos/links.txt','a+')) as f:
            f.write(value+'\n')
            f.close()                        
            #print(value)


'''----------------------Extraindo conteudo-----------------------------'''


def extrair_conteudo(content):
    urls_visitadas = set()
    urls_validas = set()
    arq = open('/home/rafael/Projetos_Python/Projetos_Online/Arquivos/links.txt', 'r')
    texto = arq.readlines()
    
                

    for linha in texto:
        if linha not in urls_visitadas:
            for index, linha in enumerate(texto):
                url_next = requests.get(linha)
                souper = BeautifulSoup(url_next.text, 'lxml')
                key = souper.text
                urls_visitadas.add(linha)
                urls_validas.add(linha)

                with(open('/home/rafael/Projetos_Python/Projetos_Online/Arquivos/correlation.txt','a+')) as filecorrelation:
                    filecorrelation.write(str(index)+ '  '+ linha+'\n')
                    filecorrelation.close()                        
                    
                
                    filename ='/home/rafael/Projetos_Python/Projetos_Online/Arquivos/Keys/' + str(index)+' .keys'
                    with open(filename,'a+') as f:
                        f.write(key)
                        f.close()                        
                        arq.close()

extrair_conteudo(links)


'''----------------------Acessando proximos links----------------------------'''

arq = open('/home/rafael/Projetos_Python/Projetos_Online/Arquivos/links.txt', 'r')
linha_arquivo = arq.readlines()


def crawler(content):   
    linha_visitadas = set()
    next_linha = set()       

    for linha in linha_arquivo:
        if url not in linha_arquivo:
            if linha not in linha_visitadas:
                linha_visitadas.add(linha)
                                      
                next_url = requests.get(linha)
                bsoup = BeautifulSoup(next_url.text, 'lxml')
                print(linha)   

                for tag in bsoup.find_all('a', href=True):
                    if tag['href'].startswith('http'):
                        next_linha.add(tag['href'])
                        print(next_linha)

                return linha

    
    
   
linha = crawler(links)
 
 
try:
    crawler(linha)
except:
    print("Error", sys.exc_info()[0])
    raise
    