def medias_por_inicial(dic_nome):
    lista_nome=list(dic_nome.keys())
    lista_notas=list(dic_nome.values())
    lista_iniciais=[]
    a=''
    i=0
    for a in lista_nome:
        if a[0] not in lista_iniciais:
            lista_iniciais.append(a[0])
    lista_medias=[0]*len(lista_iniciais)
    while i<len(lista_iniciais):
        j=0
        z=0
        while j<len(lista_nome):
            if lista_nome[j][0]==lista_iniciais[i]:
                lista_medias[i]+=lista_notas[j]
                z+=1
            j+=1
        lista_medias[i]/=z
        i+=1
    dic=dict(zip(lista_iniciais,lista_medias))
    return dic
dic_nome={'Andrew Ayres': 6, 'FÃ¡bio Ikeda': 10, 'FÃ¡bio Kurauchi': 9, 'Raul Hage': 8, 'Fabio Beltrano': 6, 'Fernando Fulano': 9}
q=medias_por_inicial(dic_nome)
print(q)