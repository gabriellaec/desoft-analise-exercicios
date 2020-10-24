x=0
lista = []
programa = True
while programa==True:
	lista[x] = int(input("Digite um número: "))
	if lista[x]<=0:
        programa = False
    else:
        x+=1
    
lista.inverse()
print (lista)