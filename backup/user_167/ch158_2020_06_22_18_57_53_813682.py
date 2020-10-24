with open ('texto.txt','r') as arquivo:
    cont=arquivo.read()
    palavras=0
    for e in cont.split():
        palavras+=1
    print(palavras)