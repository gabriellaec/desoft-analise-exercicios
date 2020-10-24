número = int(input("Digite um número:"))

contador = 0

lista = []

listareversa = []

while número > 0:
    número = int(input("Digite um número"))
    lista [contador] = número
    contador +=1
    
while contador < len(lista):
    listareversa[contador] = lista[len(lista)-(contador+1)]
    contador +=1

print (listareversa)