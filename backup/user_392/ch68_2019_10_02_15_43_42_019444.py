def separa_trios(x):
    i=0
    trios=[]
    while i < len(x)-2:
        trio = x[i] + x[i+1] + [i+2]
        trios.append(trio)
        i+=1
    return trios

    