def remove_vogais(n):
    n=[]
    i=0
    while i < len(n):
        if n[i]== 'a'or'e'or'i'or'o'or'u':
            del n[i]
        return n
            
            
    