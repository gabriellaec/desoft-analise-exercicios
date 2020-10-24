perg = True
n2 = 0
while perg == True:
    n = int(input("digite um número: "))
    if n == 0:
        perg = False
        print(n2)
    else:
        n2 = n2+n