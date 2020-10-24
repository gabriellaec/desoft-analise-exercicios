def aniversariantes_de_setembro(dicionario):
    novo_dict={}
    for nome, aniversario in dicionario:
        if aniversario[5]="7":
            novo_dict[nome]=aniversario
    return novo_dict