km=float(input('quantos km: '))
def p(km):
    if q<=200:
        y=km*0.5
        return y
    else:
        y=200*0.5+(km-200)*0.45
        return y
y=p(km)
print('{0:2f}'.format(y))