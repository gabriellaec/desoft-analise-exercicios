a=int(input('qual distância deseja percorrer?  '))
if a<=200:
    v = a*0.5
else:
    v = 100+(a-200)*0.45
print('{0:.2f}'.format(v))