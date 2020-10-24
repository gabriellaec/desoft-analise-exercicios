def remove_vogais(s):
    vogais = ['a','e','i','o','u']
    i = 0
    word = ''
    while i < len(s):
        if not s[i] in vogais :
            word += s[i]
        i+=1
    return word