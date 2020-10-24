a = input('nome do mes')
lista = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro']
i = 0
while i<12:
    if lista[i] == a:
        print(i+1)
        break
    i += 1
        
        