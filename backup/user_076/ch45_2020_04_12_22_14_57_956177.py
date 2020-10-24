x = int(input("Digite um número inteiro positivo "))
lista = []
i=0

while x>0:
    lista.append(x)
    x = int(input ("Digite outro número inteiro positivo"))

while i<=len(lista):
    print (lista[len(lista)-i])
    i+=1
    