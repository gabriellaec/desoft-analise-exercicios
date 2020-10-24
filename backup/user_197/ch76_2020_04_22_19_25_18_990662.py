def aniversariantes_de_setembro(dic1):
    dic2={}
    for i,t in dic1.items():
        if t[3]=='0' and t[4]=='9':
            dic2[i] = t
    return dic2
        
    
    