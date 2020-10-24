def aniversariantes_de_setembro (aniversarios):
    setembro={}
    for v in aniversarios.values():
        if v[3]==0 and v[4]==9:
            setembro[k]=v
    return setembro 