preço=0
with open("churras.txt","r") as arquivo:
    conteudo = arquivo.readlines()
lista_linhas=[]
for valor in range(0,len(conteudo)):
    lista_linhas.append(conteudo[valor].split(","))
for contador in range (0,len(lista_linhas)):
    preço += float(lista_linhas[contador][1])*float(lista_linhas[contador][2])