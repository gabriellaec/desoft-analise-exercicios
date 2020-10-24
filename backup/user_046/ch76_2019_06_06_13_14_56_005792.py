def aniversariantes_de_setembro(dic):
    setembro={}
    for k,v in dic.items():
        if v[4]=='9':
            setembro[k[k]]=v[6:9]
    return setembro