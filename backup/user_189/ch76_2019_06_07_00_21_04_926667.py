def aniversariantes_de_setembro(dic):
    setembro=9
    saida={}
    lisnomes=[]
    lis=[]
    for k,v in dic.items():
        lisnomes.append(k)
        lis.append(v)
    
    i=0
    
    while i<len(lis):
        if a[3:5]=='09':
            saida[lisnomes[i]]=lis[i]
   		i+=1
   	
    return saida
            
        