lista = []
num = int(input('Digite um número: '))
while num > 0 :
    lista.append(num)
    num = int (input('Digite um número: '))
i = len(lista) -1
invertida = []
while i >= 0 :
    invertida.append(lista[i])
    i += -1
print(invertida)