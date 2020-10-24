import random
d = 100
print('Você tem {0}'.format(d))
while d!=0:
    a = int(input("Aposte um valor: "))
    if a==0:
        break
    else:
        b = input("A aposta é um número ou paridade? ")
        if b==n:
            r = random.randint(1,36)
            c = int(input("Digite um número de 1 a 36: "))
            if c==r:
                d+=35*a
                print('Você tem {0}'.format(d))
            else:
                d-=a
                print('Você tem {0}'.format(d))
		elif b==p:
            
            
            
            
            