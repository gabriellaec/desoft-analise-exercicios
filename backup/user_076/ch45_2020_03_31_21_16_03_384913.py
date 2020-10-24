número = int(input("Digite um número:"))

contador = 0

lista = []

listareversa = []

while número > 0:
    número = int(input("Digite um número"))
    lista [contador] = número
    listareversa [len(lista)] = lista[contador]
    contador +=1

print (listareversa)