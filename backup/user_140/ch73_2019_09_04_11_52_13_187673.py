def remove_vogais(palavra):
    nova_palavra=""
    for i in palavra:
        if palavra[i]!="a" or palavra[i]!="e" or palavra[i]!="i" or palavra[i]!="o" or palavra[i]!="u":
            nova_palavra+=palavra[i]
    return nova_palavra