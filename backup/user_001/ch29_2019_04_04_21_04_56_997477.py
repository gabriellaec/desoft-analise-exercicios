def calcula_aumento(atual):
    if atual <= 1250.00:
        novo = atual*1.15
        return novo - atual
    else:
        novo = atual*1.1
        return novo - atual