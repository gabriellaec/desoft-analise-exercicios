def life_coutdown(pday,year):
    y = (pday*year*3650)/(24*60)
    return y
pday = input('quantos cigarros voce fuma por dia?: ')
year = input('ha quantos anos?: ')   
print('voce perdeu {0} dias da sua vida'.format(life_coutdown(float(pday),float(year))))