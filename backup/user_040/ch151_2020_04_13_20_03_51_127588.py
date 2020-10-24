def classifica_lista(x):
    n = 1
    valor_primario = ""
    valor_atual = ""
    valor_final = ""
    if len(x) > 1:
        while n < len(x):
            if valor_primario == "":
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
                
    elif len(x) <= 1:
        valor_final ="nenhum"
        
    if valor_final == "nenhum":
        return "nenhum"
    elif valor_final == "crescente":
        return "crescente"
    else:
        return "decrescente"
    