def numero_digitos(string:str):
    digitos = list("0123456789")
    return [char for char in string if char in digitos]