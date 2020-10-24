lista=[]
n=input("digite um número: ")
while n>=0:
    lista.append(n)
    n=input("digite um número: ")
    
lista_invertida = lista[::-1]

for i in lista_invertida:
    print(lista_invertida[i])