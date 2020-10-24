dic1 = {'camisa': 10,'shorts': 7}
dic2 = {'tenis': 20,'meia':18}
def lista(dic1,dic2):
    junto = []
    for i in dic1.keys():
        junto.append(i)
    for i in dic2.keys():
        junto.append(i)
    return junto
print(lista(dic1,dic2))