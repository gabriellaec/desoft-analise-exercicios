running = True
lista_n = []
while running:
    num = int(input("Número? "))
    if num > 0:
        lista_n.append(num)
    else:
        running = False
print(lista_n[::-1])