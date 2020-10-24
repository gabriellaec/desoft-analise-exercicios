def remove_vogais (string):
    b = "aeiou"
    for i in range(0,len(b)):
        a = string.lower()
        a = a.replace(b[i], "")
    return a
        
    