with open('texto.txt','r') as arquivo:
    conteudo = arquivo.readlines()
contador = 0
for texto in conteudo:
    z = texto.strip()
    x = z.split(" ")
    for p in x:
        contador+=1
print(contador)
    