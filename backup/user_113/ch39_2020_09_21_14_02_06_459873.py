n = 999
while n != 1:
    if n[2]!=2 or n[2]!=4 or n[2]!=6 or n[2]!=8 or n[2]!=0:
        n = (3*n)+1
    else:
        n = n/2
print(n)