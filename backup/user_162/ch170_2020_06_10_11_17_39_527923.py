def apaga_repetidos(ent):
    caracs = []
    for carac in ent:
        if carac not in caracs:
            caracs.append(carac)
        else:
            ent.replace(carac, "*")
            

    return ent
    