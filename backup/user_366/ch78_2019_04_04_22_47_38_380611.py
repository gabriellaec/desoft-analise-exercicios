def calcula_tempo(atletas):
    tempos = {}
    for k, v in atletas.items():
        v = (200/v)**(1/2)
        tempos[k] = v
    return tempos

dici = {}
pergunta_nome = input("Digite o nome do atleta: ")
while pergunta_nome != 'sair':
    pergunta_aceleração = float(input("Digite a aceleração do atleta: "))
    dici[pergunta_nome] = pergunta_aceleração
    pergunta_nome = input("Digite o nome do atleta: ")
      
tempo = calcula_tempo(dici)

nome = ''
menor = 100
for k, v in tempo.items():
    if v < menor:
        menor = v
        nome = k

print(f'O vencedor é {nome} com tempo de conclusão de {menor} s')