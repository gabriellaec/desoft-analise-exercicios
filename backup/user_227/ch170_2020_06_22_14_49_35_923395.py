def apaga_repetidos(string):
    string = string.lowercase()
    string2 = ''  
    for caractere in string:
        if caractere in string2:
            caractere = '*' 
            string2 + caractere
        else:
            string2 + caractere
    
    return string2