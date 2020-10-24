def tnm(ch):
    with open(ch, 'r') as arquivo:
        
        cont = arquivo.read()
    lista = cont.split('/n')        
    p = 0
        
    for i in lista:
        new = i.split(',')
        w = float(new[1]) 
        e = float(new[2])
        p+= w*e
        return p
            
print(tnm('churras.txt'))