def esconde_senha (s):
    d='*'
    e='*'
    for i in s:
        d+=e
    j=d[:len(d)]
    return j