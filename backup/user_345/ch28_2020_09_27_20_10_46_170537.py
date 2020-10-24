i = 1

soma =[0]*100
soma[0]=1.0
v=1/2**i

while i < 100:
    soma[i] = soma[i-1] + v
    i = i + 1
    
print (soma)