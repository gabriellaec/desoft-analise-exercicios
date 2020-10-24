lista=[]
while True:
    num=int(input("Digite um número inteiros para guardar e um número negativo ou zero para finalizar:"))
    if num==0 or num<0:
        break
    else:
        lista.append(num)
lista.reverse()
print(lista)