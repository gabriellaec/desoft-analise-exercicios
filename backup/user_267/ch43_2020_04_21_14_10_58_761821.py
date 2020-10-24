lista = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro']
pergunta = int(input('Qual o número do mês? '))
if pergunta <= 12:
    num = pergunta-1
    lista[num] = mes
    return mes