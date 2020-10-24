def lista_caracteres(string):
    return "".join(letras for letras in string if letras not in'aeiou')