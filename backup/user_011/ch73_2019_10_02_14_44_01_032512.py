def remove_vogais(string):
    string_sem = ''
    for letra in string:
        if letra != "a" and letra!= "e" and letra!="i" and letra!= "o" and letra != "u":
            string_sem = string_sem + letra
    return string_sem