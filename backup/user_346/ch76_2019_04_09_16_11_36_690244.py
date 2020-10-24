def aniversariantes_de_setembro(dicionario):
    novo_dict={}
    for nome, aniversario in dicionario.itens():
        if aniversario[4]="9":
            novo_dict[nome]=aniversario
    return novo_dict