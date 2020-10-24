import random
dinheiro = 100
game = True

while game == True:
    v = float(input())
    if v == 0:
        game = False
        break
    e = str(input(""))
    if e == "n":
        n = int(input(""))
        s = random.randint(0,36)
        if n == s:
            dinheiro+(35*v)
        else:
            dinheiro -= 10
    elif e == "p":
        s = random.randint(0,36)
        if s%2 == 0:
            par = True
        if s%2 != 0:
            par = False
        a = str(input(""))
        if a == "p" and par == True:
            dinheiro += v
        elif a == "i" and par == False:
            dinheiro += v
        else:
            dinheiro -= v



    
    
