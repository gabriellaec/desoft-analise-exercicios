from random import randint
rdn = randint (0,36)
i=100
while i>= 0:
    i-=1
    print (i)
    a = input("A aposta é um número ou paridade?")
    if a == "n":
        ch = int(input('Número de 0 a 36: '))
        if ch == 0:
            return False
        elif ch == rdn:
            i += 35 *ch
        else:
            i -= ch
    elif a == "p":
        ch = int(input("Número de 0 a 36: "))
        k = input("É par ou ímpar?:")
        if ch == 0:
            return False
        elif k%2==0 and rdn%2==0 or k%2!=0 and rdn%2!=0:
            i += ch
        else:
            i -= ch
            
    print (i)
        