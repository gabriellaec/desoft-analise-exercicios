def junta_listas (listadelistas):
    totaldelistas = len(listadelistas)
    i =0
    junção = []
    while i < totaldelistas:
        x = listadelistas[i]
        j = 0
        while j<len(x):
            junção.append(x[j])
            j+=1
        i+=1
    return junção
        
