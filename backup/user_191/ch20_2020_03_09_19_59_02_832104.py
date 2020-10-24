d=int(input('Dist.'))
if d<=200:
    p=0.5*d
    round(p,2)
    return p
else:
    p=200*0.5+(d-200)*0.45
    round(p,2)
    return p