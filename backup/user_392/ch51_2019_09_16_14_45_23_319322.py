def estritamente_crescente(x):
    lis = []
    i = 1
    lis.append(x[0])
    ultimo = x[0]
    while i < len(x):
        if x[i] > ultimo:
            lis.append(x[i])
            ultimo = x[i]
        i+=1
        
    return lis
   
