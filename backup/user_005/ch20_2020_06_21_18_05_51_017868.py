i = float(input('quantos km voce vai percorrer?:'))
if i <= 200:
    p = 0.5*i
else: 
    p = 200*0.5 + (i-200)*0.45
print ('{:.2f}'.format(p)) 