def interseccao_valores(dic1,dic2):
    junto = []
    
    
    for i in dic1.values():
        if i not in junto:
            junto.append(i)
    for i in dic2.values():
        if i not in junto:
            junto.append(i)
    return junto
print(interseccao_valores(dic1,dic2))   