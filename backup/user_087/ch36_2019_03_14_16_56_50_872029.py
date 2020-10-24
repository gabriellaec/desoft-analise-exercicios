n=int(input("numero: "))

def primos(n):
    divisores=0
    k=1
    while k<= n:
        if n%k == 0:
            divisores+=1
        k+=1
    
    if divisores == 2:
        return True
    else:
        return False
        
print(primos(n))