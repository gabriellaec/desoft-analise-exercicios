di = int(input())
tj = int(input())
mo = di
c = 1
while c < 24:
    mo = mo * tj
    print("{0}".format(mo))
    c += 1
print("{0}".format(mo - di))