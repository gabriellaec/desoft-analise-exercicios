def aniversariantes_de_setembro(aniversarios):
    stmb={}
    for nome,aniversario in aniversarios.items():
        if aniversario[3]==0 and aniversario[4]==9:
            stmb[nome]=aniversario
    return stmb