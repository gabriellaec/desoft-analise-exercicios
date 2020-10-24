def total_do_semestre_por_bairro (d):
    dici = {}
    for j, i in d.items():
        s = 0
        for c in range(len(i)):
            if c >= 6:
                s += i[c]
        dici[j] = s
    return dici     

def bairro_mais_custoso (d):
    a = total_do_semestre_por_bairro(d)
    li = []
    for i in a.values():
        li.append(i)
    b = max(li)
    c = li.find(b)
    k = 'a'
    count = 0
    for  j in a.keys():
        if count == c:
            k = j
        count +=1
    return k