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
        
tempo = dict()
for i in atletas:
    tempo[i] = (200/atletas[i])**(1/2)

tempo[menor] = tempo[pessoa]
for i in tempo:
    if tempo[i] < tempo[menor]:
        menor = i

print("O vencedor é {0} com tempo de conclusão de {1} s".format(menor,tempo[menor]))