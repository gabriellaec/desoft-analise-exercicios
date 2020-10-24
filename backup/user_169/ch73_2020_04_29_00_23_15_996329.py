def remove_vogais(string):
    
    i=0
    lista2=[]
    lista3=[]
    while i<len(string):
        if string[i]=='a'or string[i]=='e' or string[i]=='i' or string[i]=='o' or string[i]=='u':
             lista2.append(string[i])
        
        else:
            lista3.append(string[i])
        i+=1

    return ''.join(lista3)
            
   