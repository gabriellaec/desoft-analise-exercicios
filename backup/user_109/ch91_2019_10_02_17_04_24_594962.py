with open('palavra.txt', 'r') as arquivo:
    conteudo = arquivo.read()


lista_conteudo = conteudo.split()
palavras_com_a = []
i = 0

while i < len(lista_conteudo):
    if lista_conteudo[i][0] == 'A' or lista_conteudo[i][0] == 'a':
        palavras_com_a.append(lista_conteudo[i])
    i += 1

print(len(palavras_com_a))