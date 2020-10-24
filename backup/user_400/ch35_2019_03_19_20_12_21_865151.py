di = float(input())
dm = float(input())
tj = float(input()) + 1
mo = di
c = 1
mo = mo * tj
print("{0}".format(mo))
while c < 24:
    mo = mo + dm
    mo = mo * tj
    print("{0}".format(mo))
    c += 1
print("{0}".format(mo - di))