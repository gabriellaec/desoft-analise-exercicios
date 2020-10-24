pa = [0]*100
pa[0] = 1

a = 1
while a<100:
    pa[a] = pa[a-1]*(1/2)
def soma(a):
    y = ((+pa[99])*100)/2
    return y
print(soma(a))