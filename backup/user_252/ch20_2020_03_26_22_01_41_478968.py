km=float(input('quantos km: '))
def y(q):
    if q<=200:
        y=q*0.5
        return y
    elif q>200:
        y=200*0.5+(q-200)*0.45
        return y
print('{0:2f}'.formta(y))