def libras_para_kg(libras):
    if libras > 0:
        kg = libras*(0.453592)
    return float("{0:.6f}".format(kg))