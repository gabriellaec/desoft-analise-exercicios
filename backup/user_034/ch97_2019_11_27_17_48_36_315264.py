def total_do_semestre_por_bairro(x):
    dic={}
    key = ''
    a=[]
    i=5
    k=0
    for e in x:
        if e not in key:
            key = e
            dic[key]=[]
            while i <=11:
                a.append(x[e][i])
                i+=1
    while k < len(a):
        j=a[k]+a[k+1]
        k+=1
    dic[key].append(j)
    return dic