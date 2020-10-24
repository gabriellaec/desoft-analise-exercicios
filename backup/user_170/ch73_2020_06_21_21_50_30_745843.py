def remove_vogais(palavra):
    for i in range(len(palavra)):
        stripped = palavra.replace("a","").replace("e","").replace("i","").replace("o","").replace("u","")
    return stripped