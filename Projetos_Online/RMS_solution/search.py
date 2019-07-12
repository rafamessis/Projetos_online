from bs4 import BeautifulSoup
import requests

url = requests.get('http://www.python.org')

'''Extraindo Titulo das paginas'''

def extrair_title(content):
    soup = BeautifulSoup(content,'lxml')
    tag = soup.find('title',text=True)


    if not tag:
        return None

    return tag.string.strip()

titulo = extrair_title(url.text) #Passando o conteudo do site
with open('Titulo.html', 'w') as f:
    f.write(titulo)

    print(titulo)



'''Extraindo links das paginas'''

def extrair_links(content):
    soup = BeautifulSoup(content,'lxml')
    links = set()                          # set() tipo uma lista porem faz um agregado de informação sem uma ordem


    for tag in soup.find_all('a', href=True):
        if tag['href'].startswith('http'):
            links.add(tag['href'])

    return links

links = extrair_links(url.text) #Passando conteudo do site
print(links)



'''Extrair conteudo'''

def extrair_conteudo(content):
    soup = BeautifulSoup(content, 'lxml')
    pagina = soup.text

    return pagina

paginas = extrair_conteudo(url.text)
print(paginas)




'''Navegando nos sites '''

def crawler(starts_url):
    seen_urls = set([starts_url])
    available_urls = set([starts_url])


    while available_urls:
        url = available_urls.pop()

        try:
            content = requests.get(url, timeout=3).text
        except Exception:
            continue

    for link in extrair_links(content):
        if link not in seen_urls:
            seen_urls.add(link)
            available_urls.add(link)

    for conteudo in extrair_conteudo(content):
        if link in extrair_links(content):
            with open('Conteudo_sites.html','w') as f:
                f.writelines(conteudo)
                print(conteudo)




try:
    crawler('https://www.python.org')

except KeyboardInterrupt:
    print()
    print('Acabou')




