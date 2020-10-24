lista=[]
while True:
    numero=int(input('Numero inteiro: '))
    if numero > 0:
        lista.append(numero)
    else:
        break
for i in range(len(lista)-1, -1, -1):
    print(lista[i])