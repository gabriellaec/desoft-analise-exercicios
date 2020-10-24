dic1={'Ibiuna':1,'São Paulo':3}
dic2={'Vodka':'laikinha','Cachaça':'BoaZinha','Brejinha':'Glacial'}
def interseccao_valores(dic1,dic2):
    keys=[]
    for k1,v in dic1.items():
        keys.append(v)
    for k2,v in dic2.items():
        keys.append(v)
        
    return keys
print(interseccao_valores(dic1,dic2))