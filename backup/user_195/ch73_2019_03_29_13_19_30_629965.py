def remove_vogais(p):
    i=0
    while i<len(p):
        if p[i]=="a" or p[i]=="e" or p[i]=="i"  or p[i]=="o" or p[i]=="u":
            del p[i]
        i+=1
    return p