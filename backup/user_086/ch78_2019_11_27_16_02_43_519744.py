dicionario1={}
chave=input('digite o nome do atleta ')

#dic1={atleta1:aceleração} muv deltas/deltat=a*deltat deltat=(deltas/acel)**1/2
#dic2={atleta1:tempo}
def calcula_tempo(dic1):
    dic2={}
    for i in dic1:
        dic2[i]=(200/dic1[i])**(1/2)
    return dic2

while chave!='sair':
    valor=input('digite o valor da aceleração do atleta ')
    dicionario1[chave]=valor
    chave=input('digite o nome do atleta ')
    
def calcula_tempo(dicioAtletas):
    AtletaETempo = {}
    vencedor = 0
    tempo = 0
    if dicioAtletas != {}:
        for atleta in dicioAtletas:
            aceleracao = dicioAtletas[atleta]
            TempoDeProva = (200/aceleracao)**0.5
            AtletaETempo[atleta] = TempoDeProva

    for atleta in AtletaETempo:
        if vencedor == 0:
            vencedor = atleta
            tempo = AtletaETempo[atleta]
        elif AtletaETempo[atleta] < tempo:
            vencedor = atleta
            tempo = AtletaETempo[atleta]
    
    return 'O vencedor é {0} com tempo de conclusão de {1} s'.format(vencedor,tempo)
    
NomeEAceleracao = {}

estado = 1
while estado == 1:
    nomes = input("Nome do atleta: ")
    if nomes == 'sair':
        estado = 0
    else:
        aceleracao = float(input("Aceleração: "))
        NomeEAceleracao[nomes] = aceleracao

resultado = print(calcula_tempo(NomeEAceleracao))
    