def aniversariantes_de_setembro(dic):
    setembro=9
    saida={}
    data=[]
    nomes=[]
    for a in dic.values():
        if a[3]==9:
            data.append(a[3])
            nomes.append(dic.keys(a[3]))
   	
    return saida
            
        