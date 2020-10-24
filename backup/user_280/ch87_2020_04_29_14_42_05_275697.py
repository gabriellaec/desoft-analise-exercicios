def lista_palavras(texto):
    with open(texto, 'r') as arquivo:
        conteudo = arquivo.read()
        palavras = conteudo.split()
        return palavras

lista = lista_palavras("churras.txt")

custo = 0
i=0
while i<len(lista):
    custo += float(lista[i][1])*float(lista[i+1][2])
    i+=1

print(custo)