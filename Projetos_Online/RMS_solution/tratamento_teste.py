import io 
import nltk
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize 
import unicodedata
import re
import string

''' ---------------------------------StopWords--------------------------------------------- '''
def extrair_stopwords():
        nltk.download("stopwords")
        stopwords = nltk.corpus.stopwords.words('portuguese')
        arquivo = open("/home/rafael/Projetos_Python/Projetos_Online/RMS_solution/Arquivos/Keys/0 .keys") 
        linha = arquivo.read() 
        palavra = linha.split()
 
        for leitura in palavra:
                if not leitura in stopwords:                
                        appendFile = open('/home/rafael/Projetos_Python/Projetos_Online/RMS_solution/Arquivos/Stopwords/keysfilteredtext.txt','a')
                        appendFile.write("\n " + "  " + leitura)
                        appendFile.close()

extrair_stopwords()
                

'''----------------------------------Remover espaço entre as palavras-----------------------------'''


def extrair_espaco():

        arquivo = open("/home/rafael/Projetos_Python/Projetos_Online/RMS_solution/Arquivos/Keys/0 .keys")

        arquivo_arr = [palavra.strip() for palavra in arquivo.split(',')]

        for leitura in arquivo_arr:
                if not leitura in stopwords:
                        appendFile = open('/home/rafael/Projetos_Python/Projetos_Online/RMS_solution/Arquivos/Stopwords/keysfilteredtext.txt','a')
                        appendFile.write("\n " + "  " + leitura)
                        appendFile.close()

extrair_espaco()

