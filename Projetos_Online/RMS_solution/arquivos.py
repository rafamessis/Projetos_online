from bs4 import BeautifulSoup
import requests


def extrair_links(content):
    soup = BeautifulSoup(content,'lxml')
    links = set()                          # set() tipo uma lista porem faz um agregado de informação sem uma ordem


    for tag in soup.find_all('a', href=True):
        if tag['href'].startswith('http'):
            links.add(tag['href'])

    return links
    print(links) #para poder ver os links

'''Extrair conteudo'''

def extrai_conteudo(start_url):
    seen_url = set([start_url])
    available_url = set([start_url])


    while available_url: #Enquanto lista de url são validas, faça!!
        url = available_url.pop() # add na lista de url

        try:
            content = requests.get(url, timeout=3).text # Se site não responder em 3 segundos, salte-o
        except Exception:
            continue



        for link in extrair_links(content): #Para todos links extraidos na lista de links
            if link not in seen_url:
                seen_url.add(link)
                available_url.add(link)


        titulo = extrair_links(content)

        if titulo:
            with open('conteudo_paginas.html','w')as f:
                f.write(content.text)

        print(titulo)




if __name__ == '__main__':

    extrai_conteudo('httṕs://www.python.org')







