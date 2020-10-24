with open('palavras.txt','r') as arquivo:
    conteudo= arquivo.read()
def contador_a(conteudo):
    i=0
    contador=0
    n=len(conteudo)
    while i<n:
        if conteudo[i]== 'a':
            contador+=1
            i+=1
        return contador
print(contador_a(conteudo))