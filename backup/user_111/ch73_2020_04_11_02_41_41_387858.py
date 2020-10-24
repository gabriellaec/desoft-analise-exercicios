def remove_vogais(palavra):
    i=0
    vogais="aeiou"
    for i in range(len(palavra)):
        palavra =palavra.replace(vogais[i],"")
    return palavra