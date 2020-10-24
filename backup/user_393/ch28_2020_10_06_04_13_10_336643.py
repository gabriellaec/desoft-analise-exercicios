#Solução com while
soma= 0
x= 0 
while(x<=99):
    soma= soma + 1/(2**x)
    x= x + 1
    
print(soma)

#Solução com for
soma= 0
for k in range(0,100):
    soma= soma + 1/(2**k)
print(soma)