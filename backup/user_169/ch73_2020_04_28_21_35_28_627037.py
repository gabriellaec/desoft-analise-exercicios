def remove_vogais(string):
    
    i=0
    
    while i<len(string):
        if string[i]=='a'or string[i]=='e' or string[i]=='i' or string[i]=='o' or string[i]=='u':
            return string.split(string[i])
            
   