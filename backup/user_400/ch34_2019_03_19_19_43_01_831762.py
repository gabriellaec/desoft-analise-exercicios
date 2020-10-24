di = float(input())
tj = float(input()) + 1
mo = di
c = 0
while c < 24:
    mo = mo * tj
    print("{0}".format(mo))
    c += 1
print("{0}".format(mo - di))