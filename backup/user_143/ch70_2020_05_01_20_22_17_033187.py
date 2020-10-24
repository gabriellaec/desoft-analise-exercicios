def esconde_senha (s):
    d='*'
    e='*'
    for i in s:
        d+=e
    d=d-e
    return d