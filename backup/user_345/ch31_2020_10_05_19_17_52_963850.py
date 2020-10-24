eh_primo = True
n = int(input('Digite um número: '))
if (n == 0)or (n == 1):
    eh_primo = False
    print (eh_primo) 
elif n == 2:
        print (eh_primo)
if n > 2:
    if n % 2== 0:
        eh_primo=False
        print(eh_primo)
    else:
        x =3
        while(x <= n):
            if n % x == 0:
                eh_primo = False 
                n+=1
print (eh_primo)
                print (eh_primo)
                    break
            x=x+2
        if x==n:
            print (eh_primo)
  
          