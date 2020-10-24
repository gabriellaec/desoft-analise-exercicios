elementos=[]
soma = 0
usuario = int (input("Digite valores. Qnd quizer parar, digite 0: "))
i=0
while usuario != 0:
    elementos.append(usuario)
    usuario = int (input("Digite valores. Qnd quizer parar, digite 0: "))
for i in range (0,len(elementos)):
    soma+=elementos[i]
print (soma) 
