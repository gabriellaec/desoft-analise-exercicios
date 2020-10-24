arquivo = open("palavras.txt","r")
conteudo = arquivo.read()
i = 0
contador_de_a = 0
while i < len(conteudo):
    if conteudo[i][:1] == "a" or conteudo[i][:1] == "A":
        contador_de_a += 1
    i += 1
print (contador_de_a)