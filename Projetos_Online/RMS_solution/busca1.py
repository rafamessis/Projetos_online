import requests
from bs4 import BeautifulSoup
import sys

url = requests.get('http://www.google.com')
soup = BeautifulSoup(url.text, 'lxml')



'''Extraindo titulo da pagina'''

def extrair_titulo(content):
    tag = soup.find('title', text=True)

    if not tag:
        return None
    return tag.string.strip()

titulo = extrair_titulo(url.text)

#print(titulo)

'''Extrair links das Paginas'''

def extrair_links(content):
    links = set()

    for tag in soup.find_all('a', href=True):
        if tag['href'].startswith('http'):
            links.add(tag['href'])
    return links

links = extrair_links(url.text)

#print(links)

'''Extraindo conteudo da Pagina'''

def extrair_conteudo(starts_url):
    urls_visitadas = set([starts_url])
    urls_validas = set([starts_url])

    '''while urls_validas:
        urls_validas.pop()

        try:
            content = requests.get(url,timeout=3).text
        except Exception:
            continue
    '''
            
    for link in extrair_links(links):
        if link not in urls_visitadas:
            urls_validas.add(link)
            urls_visitadas.add(link)
            conteudo = soup.text
            
    return conteudo
      
    
    

conteudo = extrair_conteudo(url.text)
#print(conteudo)

'''Criando o Crawler'''

def crawler(starts_url):
    urls_visitadas = set([starts_url])
    urls_validas = set([starts_url])
   

    while urls_validas:
        url = urls_validas.pop()

        try:
            content = requests.get(url,timeout=3).text
        except Exception:
            continue
                
        for link in extrair_links(content):
            if link not in urls_visitadas:
                for index, value in enumerate(links):
                    urls_visitadas.add(link)
                    urls_validas.add(link)
                    with(open('correlation.txt','a+')) as filecorrelation:
                        filecorrelation.write(str(index)+ '  '+ value+'\n')
                        filecorrelation.close()                        
                        print(value)

                        key = extrair_conteudo(value)
                        filename =str(index)+' .keys'
                        with open(filename,'a+') as f:
                            f.write(key)
                            f.close()
       



try:
    crawler('http://www.google.com')
except:
    print('Error',sys.exc_info()[0])
    raise
        






