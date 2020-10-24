def conta_bigramas(a):
    dicionario = {}
    for i in range(0,len(a),1):
        b = a[i:i+2]
        c = len(b)
        #print (c)
        if c == 2:
            if b not in dicionario:
                dicionario[b] = 1

            else:
                dicionario[b] += 1

    return dicionario