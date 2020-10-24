def remove_vogais(string):
    for letra in string:
        if letra=='a' or letra=='e' or letra=='i' or letra=='o' or letra=='u':
            string=string.replace(letra, "")
    return string