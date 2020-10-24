def conta_bigramas(string):
    dic = {}
    i = 2
    dic[bigrama] = 0
    bigrama = string[0]+string[1]
    while i < len(string) - 1:
        bigrama = string[i] + string[i+1]
        i+=1
    return dic