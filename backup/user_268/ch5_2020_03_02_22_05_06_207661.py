def libras_para_kg(pd):
    kg = (pd/2) - 1/10*(pd/2)
    return kg
print ('{0: .6f}'.format(libras_para_kg))