def junta_nome_sobrenome(nome, sobrenome):
    nes=[]
    i=0
    while i<len(nome):
        nes.append(nome[i]+" "+sobrenome[i])
        i=i+1
    return nes
    