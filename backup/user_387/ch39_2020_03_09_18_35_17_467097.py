def eh_par(a):
    if a%2 == 0:
        return True
    else:
        return False

def collatz(a):
    b = 1
    while a != 1:
        if eh_par(a) == True:
            a/=2
            b+=1

        else:
            a = 3*a+1
            b+=1
    return(b)

coll = 1

for number in range(1,1000):
    
    if collatz(number) > collatz(coll):
        coll = number 


print(coll)

    