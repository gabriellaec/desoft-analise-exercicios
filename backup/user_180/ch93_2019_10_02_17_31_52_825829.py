def munchhausen(numero):
    munchhausen = 0
    numero_string = str(numero)
    if numero < 1:
        return False
    if len(numero_string) >= 1:
        for algarismo in numero_string:
            alg = int(algarismo)
            munchhausen = munchhausen + (alg**alg)
    if numero == munchhausen:
        return True
    elif numero != munchhausen:
        return False