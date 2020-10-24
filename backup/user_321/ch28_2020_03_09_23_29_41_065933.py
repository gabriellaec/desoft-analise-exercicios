i = 0
l = [0]*99
l[0] = 1
while (i < 99):
    l[i] = 1 + l[i-1]/2
    i = i+1
print (sum(l))