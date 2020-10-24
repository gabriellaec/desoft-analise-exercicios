x = float(input('quantos km? '))
if x<=200:
    print ('{0:.2f}'.format(x*0.5))
else:
    print ('{0:.2f}'.format(x*0.45))