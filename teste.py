import requests
from bs4 import BeautifulSoup
import urllib.request
import sys


url = requests.get('https://www.google.com/')
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

                while urls_validas:
                    url = urls_validas.pop()

                    try:
                        content = requests.get(url_next,timeout=3).text
                    except Exception:
                        continue 

                with(open('/home/rafael/Projetos_Python/Projetos_Online/Arquivos/correlation.txt','a+')) as filecorrelation:
                    filecorrelation.write(str(index)+ '  '+ linha+'\n')
                    filecorrelation.close()                        
                    
                
                    filename ='/home/rafael/Projetos_Python/Projetos_Online/Arquivos/Keys/' + str(index)+' .keys'
                    with open(filename,'a+') as f:
                        f.write(key)
                        f.close()                        
                        arq.close()




'''----------------------Acessando proximos links----------------------------'''

def crawler(content):
    urls = set()
    urls_visitadas = set()
    urls_validas = set()
    arq = open('/home/rafael/Projetos_Python/Projetos_Online/Arquivos/links.txt', 'r')
    texto = arq.readlines() 

    
    for linha in texto:
        url_next = requests.get(linha)
        souper = BeautifulSoup(url_next.text, 'lxml')
        if linha not in urls_visitadas:
            urls_visitadas.add(linha)
            urls_validas.add(linha)
            for tag in souper.find_all('a', href=True):
                if tag not in urls_validas:
                    if tag['href'].startswith('http'):
                        urls.add(tag['href'])
                        #print(urls)
    while urls_validas:
        url = urls_validas.pop()

        try:
            content = requests.get(urls,timeout=3).text
        except  Exception:
            continue 


    for index, value in enumerate(urls):
        if value in urls:
            with(open('/home/rafael/Projetos_Python/Projetos_Online/Arquivos/links.txt','a+')) as f:
                f.write(value+'\n')
                f.close()                        
                print(value)

   
crawler(url.text)
extrair_conteudo(url.text)
 
try:
   crawler(content)
except:
    print("Error", sys.exc_info()[0])
    raise
    