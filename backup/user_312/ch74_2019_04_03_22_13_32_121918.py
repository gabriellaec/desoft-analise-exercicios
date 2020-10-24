def conta_bigramas(string):
    bigramas={}
    counter=0
    while counter<len(string)-1:
        if string[counter:counter+2] in bigramas:
            bigramas[string[counter:counter+2]]+=1
        else:
            bigramas[string[counter:counter+2]]=1
        counter+=1
    return bigramas