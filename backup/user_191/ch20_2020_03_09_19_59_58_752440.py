d=int(input('Dist.'))
if d<=200:
    p=0.5*d
    print('{0:.2f}'.format(p))
else:
    p=200*0.5+(d-200)*0.45
    print('{0:.2f}'.format(p))