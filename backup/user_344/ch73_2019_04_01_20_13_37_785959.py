def remove_vogais(string):
    c=0
    vogais=[a,e,i,o,u]
    while i< len(string):
        string = string.lower()
        c+=1
        if vogais[c] in string:
            del vogais[c]
    return string

       
        
                 