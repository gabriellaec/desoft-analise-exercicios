with open("palavras.txt", "r") as arquivo: 
    conteudo = arquivo.read()

palavras_separadas = conteudo.split()

print(palavras_separadas)

i = 0
n_palavras_a = 0
while (i < len(palavras_separadas)):
    if(palavras_separadas[i][0] == "a" or palavras_separadas[i][0] == "A"):
        n_palavras_a = n_palavras_a + 1
    i = i + 1

print(n_palavras_a)