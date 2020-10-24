def conta_letras(l):
    dic = {}
    for i in l:
        for e in i:
            if e in dic:
                dic[e] +=1
            else:
                dic[e] = 1