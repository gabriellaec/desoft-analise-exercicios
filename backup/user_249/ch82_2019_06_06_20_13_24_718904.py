txt='apartamento'
def primeiras_ocorrencias(txt):
    dic={}
    x=0
    for i in txt:
        if i not in dic:
            dic[i]=x
        x+=1
    
    
    
    return dic