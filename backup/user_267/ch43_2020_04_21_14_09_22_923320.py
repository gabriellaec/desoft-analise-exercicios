pergunta = int(input('Qual o número do mês? '))
lista = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro']
def acha(pergunta, lista):
    num = pergunta-1
    return lista[num]