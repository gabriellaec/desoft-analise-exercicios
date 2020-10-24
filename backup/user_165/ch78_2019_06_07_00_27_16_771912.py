dicionario_atletas = {"Nome1": 1, "Nome2":2,"Nome3":1.5} 
def calcula_tempo(dicionario_atletas):
    dict = {}
    for atleta in dicionario_atletas:
        aceleracao = dicionario_atletas[atleta]
        tempo = (200/aceleracao)**0.5
        nomejogador = atleta
        dict[nomejogador] = tempo
    return dict

def qualoatletamaisrapido(calculadora_tempo):
    dicionario = {}
    input1 = input("qual o nome do atleta?")
    while input1 != "sair":
        input2 = int(input("qual a aceleração?"))
        dicionario[input1]=input2
        input1 = input("qual o nome do atleta?")
    dicionario_nomes_e_tempos = calculadora_tempo(dicionario)

    minimo =  1000000
    for i in dicionario_nomes_e_tempos:
        tempo =dicionario_nomes_e_tempos[i]
        if tempo < minimo:
            minimo = tempo
            nome =i
    return [nome, minimo]
maisrapido = qualoatletamaisrapido(calcula_tempo)
print("O vencedor é {0} com tempo de conclusão de {1} s".format(maisrapido[0], maisrapido[1]))

