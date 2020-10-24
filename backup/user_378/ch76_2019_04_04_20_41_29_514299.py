
def aniversariantes_de_setembro(aniversarios):
    aniset={}
    for nome,aniversario in aniversarios.itens():
        if aniversarios[aniversario]['mm']==9:
            aniset[nome]=aniversario
    return aniset    
print(aniversariantes_de_setembro(aniversarios))
