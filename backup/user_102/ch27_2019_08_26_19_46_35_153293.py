def vida_perdida(cigarros_por_dia, tempo_juul):
    g = cigarros_por_dia*10*tempo_juul*365/(24*60)
    return(g)


print("Vida Perdida", vida_perdida(q, s))