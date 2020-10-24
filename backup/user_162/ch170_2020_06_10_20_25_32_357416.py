def apaga_repetidos(ent):
    caracs = []
    nova_ent = ""
    for carac in ent:
        if carac not in caracs:
            caracs.append(carac)
            nova_ent += carac
        else:
            nova_ent += "*"
            

    return nova_ent
    