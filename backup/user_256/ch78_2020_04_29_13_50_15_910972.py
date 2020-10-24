nome = input("digite o nome: ")
atletas_para_tempodeprova = {}
while nome != 'sair':
    aceleracao = float(input("Digite a aceleração: "))
    tempo = (200/aceleracao)**0.5 
    atletas_para_tempodeprova[nome] = tempo
        
    nome = input("digite o nome: ")
    tmin = 10000000000 
for nome,tempo in atletas_para_tempodeprova.items():
    if tempo < tmin:
        tmin = tempo
        vencedor = nome

print ('O vencedor é {0} com tempo de conclusão de {1} s'.format(vencedor, tmin))
