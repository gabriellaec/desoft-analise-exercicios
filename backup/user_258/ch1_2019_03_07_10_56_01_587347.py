
def calcula_valor_devido (ve, nm, tj):
    M= ve*(1+tj)**nm
    return M
print (calcula_valor_devido(1000,3,0.2))