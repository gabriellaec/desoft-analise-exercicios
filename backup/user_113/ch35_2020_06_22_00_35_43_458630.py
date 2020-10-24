x=True
lista = []
while x==True:
    num = int(input ("Digite um número: "))
    if num != 0:
        lista.append(num)
    elif num == 0:
        for i in range(0, len(lista)):
            soma = lista[i] + lista[i+1]
        print (soma)
        x = False