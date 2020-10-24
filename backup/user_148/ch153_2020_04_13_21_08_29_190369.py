def agrupa_por_idade(dic):
    novo_dic = {dic1, dic2, dic3, dic4}
    
    if dic.values() <= 11:
        dic1 = {'criança': list(dic.values())}
    if 12 <= dic.values() < 18:
        dic2 = {'adolescente': list(dic.values())}
    if 18 <= dic.values() < 59:
        dic3 = {'adulto': list(dic.values())}
    if dic.values() > 59:
        dic4 = {'idoso': list(dic.values())}
        
    return novo_dic
        