lista=[]*100
s=0
i=0
while i<99:
    lista[i]=1/2**i
for e in lista:
    s+=e
    i+=1
print(s)
    