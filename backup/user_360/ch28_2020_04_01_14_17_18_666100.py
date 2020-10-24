soma = [0]*99
x=0
while x<99:
    soma[x]=1/2**x
    x+=1
    
v=sum(soma)
print(v)