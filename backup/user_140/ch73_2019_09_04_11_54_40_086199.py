def remove_vogais(palavra):
    nova_palavra=""
    for i in palavra:
        if i!="a" or i!="e" or i!="i" or i!="o" or i!="u":
            nova_palavra+=i
    if nova_palavra=="":
        return None
    return nova_palavra