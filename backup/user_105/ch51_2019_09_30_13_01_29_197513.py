def estritamente_crescente(lista):
	res = []
    if len(lista) == 0:
        return res
        
        

    
    res.append(lista[0])
    y = 0
    for i in range(len(lista)):
        
        if i+1 == len(lista):
            break
        if res[y] < lista[(i + 1)]:
            res.append(lista[(i + 1)])
            y += 1
        else:
            i += 1
    return res