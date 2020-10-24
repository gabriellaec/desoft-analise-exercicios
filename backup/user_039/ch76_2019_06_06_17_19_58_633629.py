def aniversariantes_de_setembro(dict):
    dictnovo={}
    lista=[]
    for k,v in dict.items():
        if v[4]=="9":
            dictnovo[k]=v
    return dictnovo
        
            
        
        
    