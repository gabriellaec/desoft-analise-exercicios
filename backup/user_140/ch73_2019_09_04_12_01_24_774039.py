def remove_vogais(palavra):
    nova_palavra=""
    for i in palavra:
        if i!="a" and i!="e" and i!="i" and i!="o" and i!="u":
            nova_palavra+=i
    return nova_palavra