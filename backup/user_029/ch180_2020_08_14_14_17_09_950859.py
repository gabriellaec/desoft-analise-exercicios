def ocorrencias_letras(s):
    dic = {}
    i = 0
    while i < len(s)-1:
        if i not in dic:
            dic[i]=1
            i +=1
        else:
            dic[i]= dic[i]+1
            i +=1
    return dic
    
            
         
    