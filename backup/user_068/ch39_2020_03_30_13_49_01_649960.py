def numero_de_termos(x):
x = 0
n = 0
while 0 < n < 1000:
    if n % 2 ==0:
        n = n/2
        x += 1
    else:
        n = 3*n + 1
        x +=1
return n 