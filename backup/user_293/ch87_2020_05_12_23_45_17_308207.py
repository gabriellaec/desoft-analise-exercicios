with open('churras.txt','r') as churrasco:
    chur = churrasco.read()
churchur = chur.split("\n")
soma = 0
for e in churchur:
    lista_churras = e.split(",")
    total = int(lista_churras[1])*float(lista_churras[2])
    soma += total
print(soma)