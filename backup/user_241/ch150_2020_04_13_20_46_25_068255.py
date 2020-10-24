def calcula_pi(n):
    i=1
    pi=0
    while i<n and n>1:
        pi=(6/n**2)**(1/2)
        i+=1   
    return pi
