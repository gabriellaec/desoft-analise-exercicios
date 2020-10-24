def  primeiras_ocorrencias (string):
    dic={}
    for e in range(len(string)):
        if string[e] not in dic:
            dic[string[e]]=e
    return dic
            
            
    
            
        