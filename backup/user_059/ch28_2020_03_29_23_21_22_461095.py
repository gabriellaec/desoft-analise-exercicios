x = [0]*99

i = 0
while i<99:
    x[i] = 1/2**i
    i+=1
y = sum(x)
print(y)