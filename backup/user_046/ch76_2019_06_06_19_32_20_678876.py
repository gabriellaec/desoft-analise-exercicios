def aniversariantes_de_setembro(dic):
    setembro={}
    for k,v in dic.items():
        if v[4]=='9':
            setembro[k] = v
    return setembro