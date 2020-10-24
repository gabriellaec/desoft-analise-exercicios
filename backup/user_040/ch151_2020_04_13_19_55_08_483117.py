def classifica_lista(x):
    n = 1
    valor_primario = 0
    valor_atual = 0
    valor_final = 0
    while n < len(x):
        if valor_primario == 0:
            if (x[n] - x[n-1]) > 0:
                valor_primario = "crescente"
            elif (x[n] - x[n-1]) < 0:
                valor_primario = "decrescente"
            else:
                valor_primario = "nenhum"
        else:
            if (x[n] - x[n-1]) > 0:
                valor_atual = "crescente"
            elif (x[n] - x[n-1]) < 0:
                valor_atual = "decrescente"
            else:
                valor_atual = "nenhum"
        if valor_atual != valor_primario:
            valor_final = "nenhum"
        elif valor_atual == valor_primario and valor_final == 0 or valor_final == valor_primario:
            valor_final = valor_atual
        else:
            valor_final = "nenhum"
    return valor_final
    