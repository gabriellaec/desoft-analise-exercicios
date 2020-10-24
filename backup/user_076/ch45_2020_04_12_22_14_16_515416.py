x = input("Digite um número inteiro positivo ")
lista = []
i=0

while x>0:
    lista.append(x)
    x = input ("Digite outro número inteiro positivo")

while i<len(lista):
    i+=1
    print (lista[len(lista)-i])
    