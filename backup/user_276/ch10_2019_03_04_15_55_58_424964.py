from decimal import Decimal
def libras_para_kg(x):
    y = x/2,205
    a = Decimal(y)
    output = round(a,6)
    return output