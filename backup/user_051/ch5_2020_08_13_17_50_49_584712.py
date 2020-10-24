def libras_para_kg(X):
    Y = int(X)/2.2046
    Y = "{:.6f}".format(Y)
    return int(Y)
print (libras_para_kg(5))