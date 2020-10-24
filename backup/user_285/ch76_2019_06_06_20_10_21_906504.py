def aniversariantes_de_setembro(dic):
    novodic={}
    listadatas=[]
    listanomes=[]
    for nome,data in dic.items():
        lisnomes.append(nome)
        lisdatas.append(data)
    i=0
    while i<len(listadatas):
        if listadatas[i][3:5] == "09":
            novodic[listanomes[i]]=listadatas[i]
        i+=1
    return novodic