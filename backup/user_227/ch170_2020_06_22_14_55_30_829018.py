def apaga_repetidos(string):
    string2 = ''  
    for caractere in string:
        if caractere.lower() in string2.lower():
            caractere = '*' 
            string2 += caractere
        else:
            string2 += caractere
    
    return string2