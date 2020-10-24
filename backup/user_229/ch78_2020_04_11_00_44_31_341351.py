continuar = True
atletas = {}
while continuar == True:
    pessoa = str(input('Digite o nome de um atleta: '))
    if pessoa == 'sair':
        continuar = False
    else:
        aceleracao = float(input('Qual a aceleração? '))
        atletas[pessoa] = aceleracao
        continuar == True

def calcula_tempo(atletas):
    tempo = dict()
    for i in atletas:
        tempo[i] = (200/atletas[i])**(1/2)
    return tempo

tempo[menor] = 100000
for i in tempo:
    if tempo[i] < tempo[menor]:
        menor = i

print("O vencedor é {0} com tempo de conclusão de {1} s".format(menor,tempo[menor]))