def aniversariantes_de_setembro (niver):
    dic={}
    for e,k in niver.items():
        if k[3]=='0' and k[4]=='9':
            dic[e]=k
    return dic
            
        