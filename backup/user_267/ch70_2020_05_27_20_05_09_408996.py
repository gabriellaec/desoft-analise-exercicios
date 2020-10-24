def esconde_senha(senha):
    i = 0
    esc = []
    while i < (len(senha)): 
        esc.append('*')
        i += 1
    return esc
        