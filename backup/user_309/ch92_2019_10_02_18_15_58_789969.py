def simplifica_dict(dicio):
    lista = []
    i = 0
    for i in dicio:
        if i == len(dicio):
            del dicio[i]
        else:
            y = lista.append(dicio.values)
            x = lista.append(dicio.keys)
            return x , y