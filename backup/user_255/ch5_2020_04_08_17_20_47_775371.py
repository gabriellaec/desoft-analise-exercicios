def libras_para_kg(lb):
    kg=lb/2.205
    return kg
lb=5
kg=libras_para_kg(lb)
print('O valor de kg é {:.6f}'.format(kg))