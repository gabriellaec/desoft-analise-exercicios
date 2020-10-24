import math
corredores = {}

nome = 'solta os nomin carai'
while nome != "sair":
    nome = input("Digite o valor do nome:")
    ace = float(input("Digite o valor da aceleração de {0}:".format(nome)))
    corredores[nome] = ace

def tempo_menor(dicio):
    for nome, ace in dicio.items():
        t = math.sqrt(200/ace)
        corredores[nome] = t
    return corredores

    ganhador = 'nomedomaluco'
    tmin = 1e10
    for nome, tempo in corredores.items():
        if tempo<tmin:
            tmin = tempo
            ganhador = nome
    return ganhador, tmin

tempo_menor(corredores)

print('O vencedor é {0} com tempo de conclusão de {1} s'.format(ganhador, tmin))