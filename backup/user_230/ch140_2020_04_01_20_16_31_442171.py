def faixa_notas (lista_notas):
    notas_acima=0
    notas_media=0
    notas_abaixo=0
    for nota in lista_notas:
        if nota>7:
            notas_acima+=1
        elif nota>4 and nota<8:
            notas_media+=1
        else:
            notas_abaixo+=1
    nova_lista=[0]*3
    nova_lista[0]=notas_abaixo
    nova_lista[1]=notas_media
    nova_lista[2]=notas_acima
    return nova_lista
