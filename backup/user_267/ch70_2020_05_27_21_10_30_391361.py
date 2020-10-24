def esconde_senha(senha):
    esc = ""
    for i in range(len(senha)): 
        esc += '*'
    print(esc)
        