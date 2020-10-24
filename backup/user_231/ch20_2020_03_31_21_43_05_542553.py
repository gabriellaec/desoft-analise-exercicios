d= int(input('qual a distancia que voce quer percorrer? '))
if d<200:
    p= d*0.5
else:
    p= (200*0.5) + (d-200)*0.45
print('O preço da sua passagem é {:.2f}'.format(p))
