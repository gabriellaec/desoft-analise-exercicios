def pos_arroba (email):
    for i,letra in enumerate(email):
        if letra=="@":
            return i+1