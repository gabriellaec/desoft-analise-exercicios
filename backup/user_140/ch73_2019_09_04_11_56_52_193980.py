def remove_vogais(palavra):
    nova_palavra=""
    print(palavra)
    for i in palavra:
        if i!="a" or i!="e" or i!="i" or i!="o" or i!="u":
            nova_palavra+=i
            print(nova_palavra)
    if nova_palavra=="":
        return None
    return nova_palavra