def pos_arroba(email):
    i=0
    caracteres=[email]
    while i< len(caracteres):
        if caracteres[i] == '@':
            return i
            
        else:
            i+=1
            print (i)     
        