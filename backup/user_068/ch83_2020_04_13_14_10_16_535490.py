
def medias_por_inicial(dic):
    d = {}
    for palavra in dic:
        if palavra[0] in d:
            d[palavra[0]] = (d[palavra[0]]+dic[palavra])/2
        else:
            d[palavra[0]] = dic[palavra]
    return d
print(medias_por_inicial({'Andrew Ayres': 6, 'Fábio Ikeda': 10, 'Fábio Kurauchi': 9, 'Raul Hage': 8}))
