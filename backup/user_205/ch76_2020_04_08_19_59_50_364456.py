def aniversariantes_de_setembro(dicionario):
    resultado = {}
    for nome,datas in dicionario.items():
            if dicionario[datas] == 'dd/07/aaaa':
                resultado[nome]=datas[0][1]
    return resultado
                