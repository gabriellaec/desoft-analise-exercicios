def esconde_senha(x):
    for i in x:
        x = x.replace(i,'*')
    return x