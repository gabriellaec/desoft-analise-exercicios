def capitaliza(palavra):
    for i in palavra:
        maiuscula = palavra[0].upper()
        final = maiuscula + palavra[1:]
        return final