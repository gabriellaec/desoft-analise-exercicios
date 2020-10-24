numero=int(input("Digite um número: "))
lista=[]
while numero>0:
    lista.append(numero)
    numero=int(input("Digite outro número: "))
if numero<=0:
    lista.reverse()
    print(lista)