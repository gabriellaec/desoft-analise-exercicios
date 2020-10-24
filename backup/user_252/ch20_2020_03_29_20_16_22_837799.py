km=float(input('quantos km: '))
def p(q):
    if q<=200:
        y=q*0.5
        return y
    else:
        y=200*0.5+(q-200)*0.45
        return y
y=p(km)
print('{0:2f}'.format(y))