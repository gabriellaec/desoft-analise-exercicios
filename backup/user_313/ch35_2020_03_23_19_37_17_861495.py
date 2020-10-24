a = True
s = 0
while a:
    x = int(input('Digite um numero'))
    
    if x == 0:
        a = False
        print(s)
    else:
        s = s + x