atletas = {'A': 0.01, 'B': 0.02, 'C': 0.03, 'D': 0.10}
verificar_atleta =[]
perguntar = True
while perguntar:
    x = input ("Quem você deseja medir ? ")
    if x == 'sair':
        perguntar = False
    else:
        verificar_atleta.append (x)


def calcula_tempo (atletas):
    new_dicio = {}
    for atleta, acel in atletas.items():
        t = (2*100/acel)**(0.5)
        new_dicio[atleta] = t
    resultado ={}
    for atleta in verificar_atleta:
        if atleta in new_dicio:
            resultado[atleta] = new_dicio[atleta]
    return resultado
resultado = calcula_tempo (atletas)
minimo = 10000000
for tempo in resultado.values():
    if minimo >= tempo:
        minimo = tempo
for atleta, tempo in resultado.items():
    if tempo == minimo:
        print ("O vencedor é {0} com tempo de conclusão de {1} s" .format (atleta, tempo))