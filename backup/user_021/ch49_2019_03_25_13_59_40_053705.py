ask_on=True
lista=[]
while ask_on:
    Num=int(input("Numero: "))
    if Num<=0:
        ask_on=False
    else:
        lista.append(Num)
lista=lista[::-1]
for numero in lista:
    print(numero)
        