a = 1
lista =[]
lista2=[]
while a > 0:
    b = int(input('Digite seus numeros'))
    if b !=0 :
        lista.append(b)
    a = b
count = len(lista)-1
while count >=0:
    lista2.append(lista[count])
    count -=1