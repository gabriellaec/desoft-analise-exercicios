def conta_letras(string):
    dic={}
    rep=0
    i=0
    for n in string:
        r=0
        if n in dic:
            i=0
        else:
            for k in string:
                if n==k:
                    rep+=1
            dic[n]=rep
    return dic