def aniversariantes_de_setembro(dicio):
    liste=[]
    listr=[]
    for chave,value in dicio.items():
        if value[4]=='9':
                liste.append(chave)
                listr.append(value)
    r=dict(zip(liste,listr))
    return r