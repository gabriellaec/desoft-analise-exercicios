def remove_vogais(palavra):
    abacate = ""
    for qualquer_coisa in palavra:
        if qualquer_coisa not in "aeiou":
            abacate = abacate + qualquer_coisa
        return abacate
    