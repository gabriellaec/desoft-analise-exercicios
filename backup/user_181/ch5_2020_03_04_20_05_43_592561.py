from decimal import Decimal
def libras_para_kg(lb):
    kg = lb*0.45359237
    kg = Decimal(kg)
    output = round(kg,6)
    return output