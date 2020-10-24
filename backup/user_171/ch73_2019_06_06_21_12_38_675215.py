def remove_vogais(word):
    nova=''
    vogal=['a', 'e','i','o,''u']
    for v in word:
        if vogal in word:
            word.replace(vogal,'')
    return word