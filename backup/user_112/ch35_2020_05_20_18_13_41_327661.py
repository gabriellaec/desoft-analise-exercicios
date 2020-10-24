total = 0
n = int(input('número: '))

while n != 0:
    total = total + n
    n = int(input('número: '))
    
if n == 0:
    print(total)