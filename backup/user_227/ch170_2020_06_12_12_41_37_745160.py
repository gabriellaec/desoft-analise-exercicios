def apaga_repetidos(string):

    string_final = ''

    for caractere1 in string:
        caractere1.lower()
        for caractere2 in string_final:
            caractere2.lower()
            if caractere1 == caractere2:
                caractere1 = '*'
                break
        
        string_final += caractere1
    
    return string_final