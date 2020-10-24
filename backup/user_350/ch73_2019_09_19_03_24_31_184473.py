def remove_vogais(n):
    i=0
    while i < len(n):
        if n[i]=='a' or 'e' or 'i' or 'o' or 'u':
            del str(n[i])
            i+=1
        return remove_vogais(n)
    