def conta_a(stg):
    i = 0
    s = 0
    while i < len(stg):
        if stg[i] == "a":
            s+=1
        i+=1
    return s
        