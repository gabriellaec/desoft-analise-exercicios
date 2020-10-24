def conta_bigramas(string):
    bigramas={}
    counter=0
    while counter<len(string)-1:
        bigramas[string[counter:counter+1]]+=1
    return bigramas