def traduz(lista_ingles, chavesIngles_valoresPortugues):
    lista_traduzida = []
    for palavra in lista_ingles:

        traducao = chavesIngles_valoresPortugues[palavra]
        lista_traduzida.append(traducao)
    
    return lista_traduzida