txt='apepprpipopu'
def remove_vogais(txt):
    for e in "aeiou":
        txt=txt.replace(e,'')
    return txt