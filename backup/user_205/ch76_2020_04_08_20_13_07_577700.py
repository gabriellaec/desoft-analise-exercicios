def aniversariantes_de_setembro(dicionario):
    resultado = {}
    for nome,datas in dicionario.items():
            if "07" in dicionario[datas]:
                resultado[nome]=datas[0][1]
            else:
                continue 
    return resultado
                