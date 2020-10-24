i = int(input("Digite um número inteiro: "))
lista =[]
lista_invertida=[]
while i > 0:
    lista.append(i)
    i = int(input("Digite um número inteiro: "))
for n in range(len(lista)):
    lista_invertida.append(lista[(len(lista)-1)-n])
print(lista_invertida)
    