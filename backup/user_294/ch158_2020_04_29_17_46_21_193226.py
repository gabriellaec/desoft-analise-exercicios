with open('texto.txt', 'r') as arquivo:
    a = arquivo.read()
def conta_palavras(x):
    x= a.split(' ')
    for i in len(x):
        palavras+=1
