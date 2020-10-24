def faixa_notas(notas):
    i=0
    contador_nota_abaixo_5=0
    contador_nota_de_5_ate_7=0
    contador_nota_maior_7=0
    while i < len(notas):
        if notas[i] < 5.0:
            contador_nota_abaixo_5 += 1

        elif notas[i] > 5.0 and notas[i] < 7.0:
            contador_nota_de_5_ate_7 += 1
            
        elif notas[i] > 7.0:
            contador_nota_maior_7 += 1
        i+=1
    nova_lista=[contador_nota_abaixo_5, contador_nota_de_5_ate_7, contador_nota_maior_7]
    return nova_lista