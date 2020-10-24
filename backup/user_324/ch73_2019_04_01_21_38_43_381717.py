def remove_vogais(string):
    l=[]
    for i in string:
        if i!='a' and i!='e' and i!='i' and i!='o' and i!='u':
            l.append(i)
        
    p=''
    for i in l:
        p+=i
    return p
    
    