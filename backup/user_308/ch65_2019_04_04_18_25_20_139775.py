def acha_bigramas(ds):
    big=[]
    i=0
    while i<len(ds):
        if ds[i:i+2] not in big:
            big.append(ds[i:i+2])
        i+=1
    return big
