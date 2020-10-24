def monta_dicionario (a, b):
    dic = {}
    i = 0
    while i < len(a):
        dic[a[i]] = b[i]
        i+=1
    return dic 