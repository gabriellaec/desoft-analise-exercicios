def verifica_preco(string,dic1,dic2):
    valor = 0
    for i in dic1:
        if string == i:
            for e in dic2:
                if dic1[i] == e:
                    valor = dic2[e]
    return valor