dic1 = {'A': 1, 'B': 2, 'C': 3, 'D': 4}
dic2 = {'A': 5, 'B': 6, 'C': 7, 'E': 8}
def interseccao_chaves([dic1,dic2]):
    junto = []
    
    
    for i in dic1.keys():
        if i not in junto:
            junto.append(i)
    for i in dic2.keys():
        if i not in junto:
            junto.append(i)
    return junto
print(interseccao_chaves(dic1,dic2))
       