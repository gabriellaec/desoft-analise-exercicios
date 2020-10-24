def agrupa_por_idade(dic):
    
    if dic.values() <= 11:
        dic1 = {'criança': list(dic.values())}
        return dic1
    if 12 <= dic.values() < 18:
        dic2 = {'adolescente': list(dic.values())}
        return dic2
    if 18 <= dic.values() < 59:
        dic3 = {'adulto': list(dic.values())}
        return dic3
    if dic.values() > 59:
        dic4 = {'idoso': list(dic.values())}
        return dic4