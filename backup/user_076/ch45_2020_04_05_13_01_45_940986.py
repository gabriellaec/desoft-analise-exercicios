a = int(input("Digite um número inteiro positivo: "))

i = 0 

lista = []

while a>0:
    lista[i] = a 
    a = int(input("Digite um número inteiro positivo: "))
    i+=1

listareversa = []
j=0

while j<len(lista):
    listareversa[j]=lista[len(lista)-j]
    j+=1

print(listareversa)
