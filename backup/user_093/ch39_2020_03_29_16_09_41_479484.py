n=input("Diga um numero menor que 1000 ")
while n!=1:
    if n%2==0:
        n=n-(n/2)
        print(n)
    else:
        n=3*n+1
        print(n)

    
  