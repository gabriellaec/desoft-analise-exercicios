def traduz(ingles, dicionario):
    port = []
    for ing in ingles:
        for dic in dicionario:
            if dic == ing:
                port.append(dicionairo[dic])
    return port