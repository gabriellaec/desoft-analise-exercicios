while True:
    nome = input("Digite um nome: ")
    if nome == "sair":
        break
    aceleracao = input("Qual aceleração? ")
    
def calcula_tempo(dic):
    dicionario = {}
    maior = 0
    for nome,aceleracao in dic.items():
        dicionario[nome] = ((200/aceleracao)**(1/2))
        for i in range (dicionario.values):
            if i > maior:
                maior = i
                pessoa = dicionario.keys
            
    return ('O vencedor é', pessoa, 'com tempo de conclusão de', i, 's')
