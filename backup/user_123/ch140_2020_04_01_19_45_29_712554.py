def faixa_notas(notas):
    a = 0
    men5 = 0
    ent57 = 0
    mai7 = 0
    lista_notas=[]
    while a<leno(notas):
        if notas[i]>=0 and notas[i]<5:
            men5 = men5 +1
        elif notas[i]>=5 and notas[i] <=7:
            ent57 = ent57 + 1
        elif notas[i]> 7 and notas[i]<=10:
            mai7 = mai7 +1
        a +=1
    
    lista_notas.append(men5)
    lista_notas.append(ent57)   
    lista_notas.append(mai7)
    return lista_nova