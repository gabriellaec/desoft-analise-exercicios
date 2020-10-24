meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro']
x = input()
k = 0
while k < 12:
    if x == meses[k]:
        print (k+1)
    k += 1
    