def remove_vogais(palavra):
    vogais=["a", "e", "i", "o", "u"]
    for i in palavra:
        if i in vogais:
            nova=palavra.replace(i, "")
    return nova
            
           