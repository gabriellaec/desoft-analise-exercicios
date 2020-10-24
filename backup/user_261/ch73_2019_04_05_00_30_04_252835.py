def remove_vogais(palavra):
    for e in "aeiou":
        palavra=palavra.replace(e,"")
    return palavra
