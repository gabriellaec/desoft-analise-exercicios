def apaga_repetidos(string):
    string2 = ''  
    for caractere in string.lowercase():
        if caractere in string2:
            caractere = '*' 
            string2 + caractere
        else:
            string2 + caractere
    
    return string2