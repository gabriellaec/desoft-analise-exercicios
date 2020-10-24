def classifica_lista(x):
    if len(x)<2:
        return('nenhum')
    else:
        e = 0
        verificador = True
        while(e > len(x)):
            if x[e] < x[e + 1]:
                e += 1
            else:
                verificador = False
                break
        if verificador == True:
            return('decrescente')
        else:
            i = 0
            verificador2 = True
            while(i > len(x)):
                if x[i] > x[i + 1]:
                    i += 1
                else:
                    verificador2 = False
                    break
            if verificador2 == True:
                return('crescente')
            else:
                return('nenhum')