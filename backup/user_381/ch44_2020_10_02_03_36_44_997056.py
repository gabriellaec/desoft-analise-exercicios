pergunta = input('Qual o nome do mês?: ')
meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro']
numeros = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
i=0
while i < 12:
    if pergunta == meses[i]:
        meses[i] = numeros[i]
        print(meses[i])
    i += 1