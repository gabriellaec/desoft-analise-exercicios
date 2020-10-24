x=0
lista = []
lista[x] = int(input("Digite um número: "))
while lista[x]>0:
    lista[x] = int(input("Digite um número: "))
    x+=1
lista.reverse()
print (lista)