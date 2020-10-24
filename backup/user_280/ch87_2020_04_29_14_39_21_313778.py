def lista_palavras(texto):
    with open(texto, 'r') as arquivo:
        conteudo = arquivo.read()
        palavras = conteudo.split()
        return palavras

lista = lista_palavras("churras.txt")

custo = 0
i=1
while i<len(lista) - 1:
    custo += (float(lista[i]))*(float(lista[i+1]))
    i+=3

print(custo)
