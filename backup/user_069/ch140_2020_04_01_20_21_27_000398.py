def faixa_notas (lista_notas):
    nova_lista = []
    i = 0
    s1 = 0
    s2 = 0 
    s3 = 0
    while i < len(lista_notas):
        if lista_notas[i] < 5:
            s1 += 1
        if lista_notas[i] >= 5 and lista_notas[i] <= 7:
            s2 += 1
        if lista_notas[i] > 7:
            s3 += 1
        i +=1
    nova_lista.append(s1)
    nova_lista.append(s2)
    nova_lista.append(s3)
    return nova_lista