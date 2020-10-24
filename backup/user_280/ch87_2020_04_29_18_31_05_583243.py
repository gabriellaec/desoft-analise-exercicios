def lista_palavras(texto):
    with open(texto, 'r') as arquivo:
        conteudo = arquivo.read()
        palavras = conteudo.split()
        return palavras

lista = lista_palavras("churras.txt")

custo = 0
i=2
while i<len(lista):
    custo += float(lista[i])*float(lista[i+2])
    i+=5

print(custo)