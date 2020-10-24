pg = [0]*100
pg[0] = 1
i = 1
while (i<99):
   pg[i] = pg[i-1]*(0.5**(i-1))
   i += 1
print(sum(pg))
 