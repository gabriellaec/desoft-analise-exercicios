def remove_vogais(word):
    nova=''
    vogal=['a', 'e','i','o','u']
    for x in range(len(word)):
        if word[x] not in vogal:
            nova+=word[x]
    return nova