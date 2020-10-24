def classifica_lista(x):
    if len(x)<2:
        return('nenhum')
    else:
        e = 1
        verificador = True
        while(e >= len(x)):
            if x[e-1] < x[e]:
                e += 1
            else:
                verificador = False
                break
        if verificador == True:
            return('crescente')
        else:
            i = 1
            verificador2 = True
            while(i >= len(x)):
                if x[i-1] > x[i]:
                    i += 1
                else:
                    verificador2 = False
                    break
            if verificador2 == True:
                return('decrescente')
            else:
                return('nenhum')