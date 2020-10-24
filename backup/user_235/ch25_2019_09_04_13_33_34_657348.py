x=float(input('quantos Kms vai percorrer?'))
if x<=200:
    y=0.50*x
    print(y)
else:
    y=100+0.45*(x-200)
    print(y)
