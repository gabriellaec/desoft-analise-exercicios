elementos=[]
soma = 0
while usuario != 0:
    usuario = int (input("Digite valores. Qnd quizer parar, digite 0: "))
    elementos.append(usuario)
    
for i in range (0,len(elementos)):
    soma += elementos [i]
print (soma)
