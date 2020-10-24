def apaga_repetidos(string):
    nova_string=0
    for letra in string:
        if letra not in nova_string:
            nova_string+=str(letra)
        else:
            nova_string+="*"
    return nova_string