def remove_vogais(string):
    for i in "aeiou":
        if i in string:
            string=string.replace(i,"")
    return string 
            
        