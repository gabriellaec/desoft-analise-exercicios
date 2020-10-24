def calcula_tempo(dicionario):
    nomes = list(dicionario.keys())
    dicionariot = {}
    for nome in nomes:
        t = 10/(dicionario[nome]/2)**(1/2)
        dicionariot[nome] = t
    return dicionariot

def main():
    menort = 0
    menorn = ''
    dicionario = {}
    while True:
        nome = input('digite um nome: ')
        if nome == 'sair':
            break
        else:
            aceleracao = float(input('Qual a aceleracao: '))
            dicionario[nome] = aceleracao
    dicionario = calcula_tempo(dicionario)
    lista = list(dicionario.keys())
    for nome in lista:
        if dicionario[nome] < menort:
            menort = dicionario[nome]
            menorn = nome
    print(menorn)
    