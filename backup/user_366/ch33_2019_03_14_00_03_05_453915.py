i = 1
s = 0
n = 1/(2**99)

while i < n:
    s += i
    i *= 1/2
    
print(s)