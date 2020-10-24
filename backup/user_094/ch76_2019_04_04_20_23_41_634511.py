def aniversariantes_de_setembro(niver):
    setembro = {}
    for k,v in niver.items():
        if '/09/' in v:
            setembro[k]=v  
    return setembro
