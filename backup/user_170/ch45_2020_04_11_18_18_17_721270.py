i = int(input("Digite um número in"))
lista =[]
lista_invertida=[]
while i > 0:
    lista.append(i)
    i = int(input("Digite um número in"))
for i in range(len(lista)):
    lista_invertida.append(lista[len(lista)-i])
print(lista_invertida)
    