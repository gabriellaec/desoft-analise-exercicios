def remove_vogais(string):
    string_sem = ''
    for letra in string:
        if letra != "a" or letra!= "e" or letra!="i" or letra!= "o" or letra != "u":
            string_sem = string_sem + letra
    return string_sem