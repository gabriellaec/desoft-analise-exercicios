def remove_vogais(word):
    n=str(word)
    vowel= ('a','e','i','o','u')
    for vowel in word:
        del vowel
    return n
        