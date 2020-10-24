lista=[]
while True:
    x= int(input("Digite um número:"))
    if x==0:
        break
    elif x < 0:
        break
    lista.append(x)

i= len(lista) - 1
while i >=  0:
    print(lista[i])
    i= i - 1