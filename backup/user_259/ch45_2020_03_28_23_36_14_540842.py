run = True
lista = []
while run:
    num = int(input("insira um número: "))
    if num <= 0:
        run = False
    else:
        lista.append(num)
for i in range(len(lista)):
    lista[i] = lista[len(lista)-i]
print(lista)
                      
                      
    