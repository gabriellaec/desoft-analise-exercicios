while True:
    nome = input("Digite um nome: ")
    if nome == "sair":
        break
    aceleracao = input("Qual aceleração? ")
    
def calcula_tempo(dic):
    dicionario = {}
    for nome,aceleracao in dic.items():
        dicionario[nome] = ((200/aceleracao)**(1/2))
    return ('O vencedor é', nome, 'com tempo de conclusão de', dicionario, 's')
