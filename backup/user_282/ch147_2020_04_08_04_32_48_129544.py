def mais_frequente(lista):
    count = dict()
    for palavra in lista:
        if palavra not in count:
            count[palavra] = 1
        else:
            count[palavra] += 1
    values = list(count.values())
    keys = list(count.keys())
    for e in range(len(values)):
        if max(values) == values[e]:
            return keys[e]