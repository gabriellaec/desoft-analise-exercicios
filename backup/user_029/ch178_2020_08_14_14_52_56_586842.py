def junta_nomes(a,b,c):
    lista = []
    for i in a:
        if len(a) != 0:
            for d in c:
                lista.append(i+ ' ' +d)    
    for e in b:
        if len(b) != 0:
            for f in c:
                lista.append(e+ ' ' +f)            
    return lista