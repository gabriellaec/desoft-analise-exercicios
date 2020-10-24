def quantos_uns(n):
    n==str(n)
    repeticaoes=0
    
    i=0
    while i<=len(n):
        if n[i]== "1":
            repeticaoes+=1
        i+=1
    
    return repeticaoes