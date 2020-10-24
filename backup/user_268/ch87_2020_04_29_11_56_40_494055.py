def tnm(ch):
    with open(ch, 'r'):
        
        lista = ch.split('\n')
        
        p = 0
        a = len(lista)
        
        for i in range(a):
            new = lista[i].split(',')
            p += int(new[1]) * float(new[2])
            
        return p
            
print(tnm('churras.txt'))