def conta_bigramas (string):
    dicio ={}
    i=0
    while i< len(string) -1 :
        if str(string[i]+string[i+1]) in dicio:
            dicio[string[i]+string[i+1]] += 1
        else:
            dicio[string[i]+string[i+1]] = 1
        i +=1
    return dicio