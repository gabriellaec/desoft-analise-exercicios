def aniversariantes_de_setembro(dic):
    saida={}
   	nomes=[]
    lis=[]
    for k,v in dic.items():
        nomes.append(k)
        lis.append(v)
    
    i=0
    while i<len(lis):
        if lis[i][3:5]=='09':
            saida[nomes[i]]=lis[i]
            i+=1
   	
    return saida
            
        