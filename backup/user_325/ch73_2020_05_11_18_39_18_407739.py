def remove_vogais(stg):
    i = 0
    while i < len(stg):
        if stg[i] == "a" or stg[i] == "e" or stg[i] == "i" or stg[i] == "o" or stg[i] == "u":
            stg[i].replace([i],"")
        i+=1
    return stg