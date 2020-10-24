def aniversariantes_de_setembro(dicio):
    dicio2 = {}
    for i,j in dicio.items():
        if j[3:5] == "09":
            dicio2[i] = j
            
    return dicio2