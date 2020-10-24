def troca_virgula(texto):
    with open(texto, 'r') as arquivo:
        conteudo = arquivo.read()
        trocado = conteudo.replace(',', ' ')
        return trocado

def lista_palavras(texto):
    with open(texto, 'r') as arquivo:
        conteudo = arquivo.read()
        palavras = conteudo.split()
        return palavras
    
lista = lista_palavras(troca_virgula("churras.txt"))

custo = 0
i=1
while i<len(lista):
    custo += float(lista[i])*float(lista[i+1])
    i+=3

print(custo)