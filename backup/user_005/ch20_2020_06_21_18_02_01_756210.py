i = float(input('quantos km voce vai percorrer?:'))
if i <= 200:
    p = 0.5*i
else: 
    p = 0.45*i
print ('{:.2f}'.format(p)) 