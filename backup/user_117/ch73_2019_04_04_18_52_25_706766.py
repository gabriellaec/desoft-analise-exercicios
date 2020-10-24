def remove_vogais(string):
    i=0
    list(string)
    v=['a','e','i','o','u']
    while i<len(string):
        if string[i] in v:
            del string[i]
        else:
            i+=1
    return 'string'
        
        
        