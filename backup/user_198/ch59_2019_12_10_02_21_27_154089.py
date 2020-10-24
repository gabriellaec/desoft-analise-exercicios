def conta_a(entrada):
    T=len(entrada)
    cont=0
    for i in range(0,T):
        if entrada[i]=="a":
            cont+=1
    return(cont) 