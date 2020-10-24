def tnm(ch):
    with open(ch, 'r'):
        
        lista = ch.split('\n')
        
        p = 0
        a = len(lista)
        
        for i in lista:
            new = i.split(',')
            w = float(new[1]) 
            e = float(new[2])
            p+= w*e
        return p
            
print(tnm('churras.txt'))