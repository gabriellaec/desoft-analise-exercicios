def conta_bigramas(string):
    dict= {}
    i=0
    for i in range(len(string)-1):
        bigrama= string[i] + string[i+1]
        if bigrama not in dict:
            dict[bigrama] = 1
        else:
            dict[bigrama] += 1
    return dict