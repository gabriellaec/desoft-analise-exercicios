def apaga_repetidos(string):
    string2 = ''  
    for caractere in string.lower():
        if caractere in string2:
            caractere = '*' 
            string2.append(caractere)
        else:
            string2.append(caractere)
    
    return string2