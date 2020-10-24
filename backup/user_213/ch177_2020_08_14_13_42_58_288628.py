def numero_digitos(s):
    senha = s
    dig = 0
    for c in senha:
        if c.isdigit()==True:
            dig+=1
    return dig
    