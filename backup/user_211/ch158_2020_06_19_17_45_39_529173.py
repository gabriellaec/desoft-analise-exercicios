with open('texto.txt','r') as arquivo:
    palavras=arquivo.split()
    n=0
    for i in range(0,len(palavras)):
        n+=1
    print(n)
    