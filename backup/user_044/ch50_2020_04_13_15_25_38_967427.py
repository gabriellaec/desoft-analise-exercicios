def junta_nome_sobrenome(ls1,ls2):
    esp=' '
    ls3=[]
    for i in range(len(ls1)):
        ls3.append(ls1[i]+esp+ls2[i])
    return ls3