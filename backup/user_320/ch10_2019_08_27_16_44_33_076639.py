def libras_para_kg(libras):
    if libras <= 0:
        return 0
    kg = float(libras) /2.205
    return round(kg, 6)