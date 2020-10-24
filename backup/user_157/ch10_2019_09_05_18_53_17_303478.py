def truncate(n, decimals=0):
    multiplier = 10 ** decimals
    return int(n * multiplier) / multiplier

def libras_para_kg(libras):
    kg = libras/2.2046
    kg = truncate(kg, 6)
    return kg