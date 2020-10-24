run = True
lista = []

while run:
    num = int(input("insira um número: "))
    if num <= 0:
        run = False
    else:
        lista.append(num)
lista.reverse()
print(lista)
                      
                      
    