with open('palavras.txt', 'r') as arquivo:
    conteudo = arquivo.read()
lista_palavras = conteudo.split()
i = 0
palavras_a = 0
while i < len(lista_palavras):
    palavra = lista_palavras[i].lower()
    if palavra[0] == 'a':
        palavras_a +=1
    i+=1
print(palavras_a)