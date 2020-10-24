def tnm(ch):
    with open(ch, 'r'):
        
        cont = ch.read()
        lista = cont.split('
')        
        p = 0
        
        for i in lista:
            new = i.split(',')
            w = float(new[1]) 
            e = float(new[2])
            p+= w*e
            return p
            
print(tnm('churras.txt'))