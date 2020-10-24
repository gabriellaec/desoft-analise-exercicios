def remove_vogais(palavra):
    i=0
    vogais="aeiou"
    while i<len(palavra):
        palavra=palavra.replace(vogais[i],"")
        i+=1
    return palavra