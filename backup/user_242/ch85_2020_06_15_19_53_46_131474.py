with open ('macacos-me-mordam.txt', 'r') as arquivo:
    conteudo = arquivo.readlines()
    palavras=[]
    for i in conteudo:
        separa = i.split('')
        palavras += separa
lista=[]
for i in palavras:
    separa2 = i.strip()
    separa = separa2.lower()
    lista.append(separa)