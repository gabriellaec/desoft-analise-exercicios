def aniversariantes_de_setembro(aniversariantes):
    setembro=dict()
    for i in aniversariantes:
        if '/09/' in aniversariantes[i]:
            setembro[i]=aniversariantes[i]
    return setembro