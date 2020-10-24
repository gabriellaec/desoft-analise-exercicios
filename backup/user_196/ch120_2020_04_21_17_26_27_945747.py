from random import randint
rdn = randint (1,36)
i=100
while i>= 0:
    i-=1
    print (i)
    a = input("A aposta é um número ou paridade? (n/p)")
    if a == "n":
        ch = int(input('Número de 1 a 36: '))
        if ch == 0:
            return False
        elif ch == rdn:
            i += 35 *ch
        else:
            i -= ch
    elif a == "p":
        ch = int(input("Número de 0 a 36: "))
        k = input("É par ou ímpar?: (p/i)")
        if ch == 0:
            return False
        elif k == "p":
            if rdn%2 == 0:
                i += ch
        elif k == "i":
            if rdn%2 != 0:
                i+=ch
        else:
            i -= ch
            
    print (i)
        