import nltk
from nltk.stem import RSLPStemmer
#nltk.download('rslp')


def Tokenize(sentence):
    sentence = sentence.lower()
    sentence = nltk.word_tokenize(sentence)
    return sentence

frase1 = 'Eu gosto de correr'
frase2 = 'Eu gosto do Rafael'
frase1 = Tokenize(frase1)
frase2 = Tokenize(frase2)
print('---------------------tokenizaçao---------------------')
print(frase1)
print(frase2)
print('\n')



def Stemming(sentence):
    stemmer = RSLPStemmer()
    phrase = []
    for word in sentence:
        phrase.append(stemmer.stem(word.lower()))
    return phrase

frase1 = Stemming(frase1)
frase2 = Stemming(frase2)
print('---------------------Stemming---------------------')
print(frase1)
print(frase2)
print('\n')


def RemovendoStopWords(sentence):
    stopwords = nltk.corpus.stopwords.words('portuguese')
    phrase = []
    for word in sentence:
        if word not in stopwords:
            phrase.append(word)
    return phrase


frase1 = RemovendoStopWords(frase1)
frase2 = RemovendoStopWords(frase2)
print('---------------------Stopwords---------------------')
print(frase1)
print(frase2)
print('\n')



def Train():
    training_data = []
    training_data.append({"classe":"amor", "frase":"Eu te amo"})
    training_data.append({"classe":"amor", "frase":"Você é o amor da minha vida"})
    training_data.append({"classe":"medo", "frase":"estou com medo"})
    training_data.append({"classe":"medo", "frase":"tenho medo de fantasma"})
    print("%s frases incluidas" % len(training_data))
    return training_data

dados = Train()


def Learning(training_data):
    corpus_words = {}
    for data in training_data:
        frase = data['frase']
        frase = Tokenize(frase)
        frase = Stemming(frase)
        frase = RemovendoStopWords(frase)
        class_name = data['classe']
        if class_name not in list(corpus_words.keys()):
            corpus_words[class_name] = {}
        for word in frase:
            if word not in list(corpus_words[class_name].keys()):
                corpus_words[class_name][word] = 1
            else:
                corpus_words[class_name][word] += 1
    return corpus_words

dados =Learning(dados)
print(dados)
