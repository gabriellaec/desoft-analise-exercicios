def libras_para_kg(X):
    Y = int(X)/2.2046
    return Y
t=libras_para_kg(5)
print ("{:.6f}".format(t))