lista = []
while True:
    x = int(input('Digite um valor: '))
    if x>0:
        lista.append(x)
    else: 
        break
lista.reverse()
print(lista) 
