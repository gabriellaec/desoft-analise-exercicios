def remove_vogais(palavra):
    vogais=["a", "e", "i", "o", "u"]
    for i in palavra:
        for e in vogais:
            if i==e:
                palavra=palavra.replace(i, "")
    return nova
            
           