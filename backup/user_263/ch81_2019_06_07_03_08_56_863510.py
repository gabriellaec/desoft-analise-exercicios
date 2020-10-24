def interseccao_valores(dic1,dic2):
    interseccao = []
    for valores in dic1.values():
        for v in dic2.values():
            if valores == v and v not in interseccao:
                interseccao.append(v)
                
    return interseccao