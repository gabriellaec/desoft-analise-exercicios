def esconde_senha (s):
    d='*'
    e='*'
    j='a'
    for i in s:
        d+=e
    j=d[:len(d)]
    return j