x=True
lista = []
soma = 0
while x==True:
    num = int(input ("Digite um número: "))
    if num != 0:
        lista.append(num)
    elif num == 0:
        for i in range(0, len(lista)):
            soma + lista[i]
        print (soma)
        x = False