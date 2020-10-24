#função que recebe um lista de notas 
#retorne em uma nova lista : quantos alunos possuem notas < 5, <7, >7
notas=[3, 4, 5, 5.5, 6, 9]
def faixa_notas(notas):
    i=0
    contador_nota_abaixo_5=0
    contador_nota_de_5_ate_7=0
    contador_nota_maior_7=0
    while i < len(notas):
        if notas[i] < 5:
            contador_nota_abaixo_5 += 1

        elif notas[i] >= 5.0 and notas[i] <= 7.0:
            contador_nota_de_5_ate_7 += 1
            
        elif notas[i] > 7.0:
            contador_nota_maior_7 += 1
        i+=1
    nova_lista=[contador_nota_abaixo_5, contador_nota_de_5_ate_7, contador_nota_maior_7]
    return nova_lista
print(faixa_notas(notas))