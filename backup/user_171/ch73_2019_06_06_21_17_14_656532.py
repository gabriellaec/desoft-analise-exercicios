def remove_vogais(word):
    nova=word
    vogal=['a', 'e','i','o,''u']
    for v in word:
        if v in vogal:
            nova.replace(vogal,'')
    return nova