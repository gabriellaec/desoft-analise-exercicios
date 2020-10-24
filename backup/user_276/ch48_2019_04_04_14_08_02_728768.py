nome = input(Nome de um mês:   )
meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro']
while i < len(meses):
    if nome in meses:
        ind += 1
        print(ind)
    i +=1