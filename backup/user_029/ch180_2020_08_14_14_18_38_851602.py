def ocorrencias_letras(s):
    dic = {}
    i = 0
    while i < len(s)-1:
        if s[i] not in dic:
            dic[i]=1
            i +=1
            print(dic)
        else:
            dic[i]= dic[i]+1
            print(dic)
    return dic
    
            
         
    