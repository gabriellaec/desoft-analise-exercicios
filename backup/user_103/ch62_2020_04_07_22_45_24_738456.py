def pos_arroba(email):
    i=0
    caracteres=[email]
    while i< len(caracteres):
        if caracteres[i] == '@':
            print (i)
        else:
            i+=1
            
        