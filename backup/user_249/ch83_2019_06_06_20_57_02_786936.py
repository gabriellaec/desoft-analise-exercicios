dic={'Andrew Ayres': 6, 'Fábio Ikeda': 10, 'Fábio Kurauchi': 9, 'Raul Hage': 8}
def medias_por_inicial(dic): 
    dic2={}
    x=0
    for k,v in dic.items():
        if k[0] not in dic2:
            dic2[k[0]]=v
        else:
            x+=1
            dic2[k[0]]=(dic2[k[0]]+v)/x
    return dic2
print (medias_por_inicial(dic))
          
