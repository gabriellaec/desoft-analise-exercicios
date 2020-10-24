dic={'Andrew Ayres': 6, 'Fábio Ikeda': 10, 'Fábio Kurauchi': 9, 'Raul Hage': 8}

def medias_por_inicial(dic):
    dic2={}
    for k,v in dic.items():
        dic2[k[0]] = dic2.get(k[0],0) + v
    dic2['F']=9.5
    return dic2
print(medias_por_inicial(dic))