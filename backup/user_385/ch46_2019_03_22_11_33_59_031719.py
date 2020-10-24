def letra_a(palavra):
    i=0
    c=0        
    while i<len(palavra):
        if palavra[i]=='a':
            c+=1
        i+=1    
    return c
palavra= input('palavra:')
print(letra_a(palavra))
       
       