def aniversariantes_de_setembro(dic):
    novodic={}
    listadatas=[]
    listanomes=[]
    for nome,data in dic.items():
        listanomes.append(nome)
        listadatas.append(data)
        
    for i in range(len(listanomes)):
        if listadatas[i][3:5] == "09":
            novodic[listanomes[i]]=listadatas[i]
    return novodic