
dic1={'Ibiuna':'PiuPiu','São Paulo':'Lipiupiu'}
dic2={'Vodka':'laikinha','Cachaça':'BoaZinha','Brejinha':'Glacial'}
def interseccao_chaves(dic1,dic2):
    keys=[]
    for k1,v in dic1.items():
        keys.append(k1)
    for k2,v in dic2.items():
        keys.append(k2)
        
    return keys
print(interseccao_chaves(dic1,dic2))