with open("churras.txt","r") as arquivo:
    churras = arquivo.read()
    
churras_tsv = churras.replace(","," ")
churras_lista = churras_tsv.split()

a = 0
b = 0
c = 0
soma = 0
for i in churras_lista:
    if a == 1:
        b = i
    elif a == 2:
        c = i
    elif a >= 2:
        a = 0
    else:
        b = 0
        c = 0
    soma += b * c
    
