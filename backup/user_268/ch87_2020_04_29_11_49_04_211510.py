def tnm(ch):
    with open(ch, 'r'):
        lista = ch.readlines()
        
        p = 0
        a = len(lista)
        
        for i in range(a-1):
            new = lista[i].split(',')
            p += int(new[1]) * float(new[2])
            
        return p
            
            