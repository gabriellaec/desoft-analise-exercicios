x=float(input('km?:'))
if x<=200:
    y=0.50*x
else:
    y=0.50*200+0.45*(x-200)
print('%2f'%y)