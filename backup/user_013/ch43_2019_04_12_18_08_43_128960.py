i = 1 
n = input()
if n == '':
    n = 1
    i = 0
n = int(n)    
while n != 1:
  
    if n % 2 == 0:
        n = n / 2
    else:
        n = 3*n + 1
    i += 1
print(i)