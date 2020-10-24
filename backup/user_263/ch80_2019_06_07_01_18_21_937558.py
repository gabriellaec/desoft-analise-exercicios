def interseccao_chaves(dic1,dic2):
    interseccao = []
    for key in dic1:
        for k in dic2:
            if key == k and k not in interseccao:
                interseccao.append(k)
                
    return interseccao
        
    