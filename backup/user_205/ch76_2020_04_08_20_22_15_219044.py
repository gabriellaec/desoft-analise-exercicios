def aniversariantes_de_setembro(dicionario):
    resultado = {}
    for nome,datas in dicionario.items():
            if datas[3:5]="09":
                resultado[nome]=datas
    return resultado
                