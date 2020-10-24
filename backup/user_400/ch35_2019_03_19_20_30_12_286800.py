di = float(input())
dm = float(input())
tj = float(input()) + 1
mo = di
c = 1
mo = mo * tj
print("{0}".format(mo))
mo = mo + dm
while c < 24:
    mo = mo * tj
    print("{0}".format(mo))
    mo = mo + dm
    c += 1
print("{0}".format(mo - 1 - di))