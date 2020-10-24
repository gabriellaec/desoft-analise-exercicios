dicionario_atletas = {"Nome1": 1, "Nome2":2,"Nome3":1.5} 
def calcula_tempo(dicionario_atletas):
    dict = {}
    for atleta in dicionario_atletas:
        aceleracao = dicionario_atletas[atleta]
        tempo = (200/aceleracao)**0.5
        nomejogador = atleta
        dict[nomejogador] = tempo
    return dict
dicionario = {}
x = input("qual o nome do atleta?")
while x != "sair":
    y = int(input("qual a aceleração?"))
    dicionario[x]=y
    x = input("qual o nome do atleta?")
    dicionario_nomes_e_tempos = calcula_tempo(dicionario)

total_tempo = dicionario_nomes_e_tempos 
menor_tempo = 1000
vencedor = ""
for atleta in total_tempo:
    tempo_corrido = total_tempo[atleta]
    if tempo_corrido < menor_tempo:
        vencedor = atleta
        menor_tempo = tempo_corrido
print("O vencedor é {0} com tempo de conclusão de {1}s".format(vencedor[0],menor_tempo[1]))