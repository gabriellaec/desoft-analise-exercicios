i = 0
nmes = input("Escolha um mes: ")
meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro']
while i < len(meses):
    if nmes == meses[i]:
        print(i + 1)
    i += 1
