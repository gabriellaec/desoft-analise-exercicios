def traduz(lista_ingles, dicionario):
    traducao = []
    for palavra in lista_ingles:
        for eng, port in dicionario.items():
            if palavra == eng:
                traducao.append(port)
    return traducao