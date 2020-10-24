a = input('manda um mes')
i = 0
lista=['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro']
while i < len(lista):
    if lista[i] == a:
        print (i+1)
    i += 1
