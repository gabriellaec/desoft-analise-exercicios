def remove_vogais(n):
    i=0
    while i < len(n):
        if n[i]== 'a'or n[i]=='e'or n[i]=='i'or n[i]=='o'or n[i]=='u':
            del n[i]
        i+=1
    return n
            
            
    