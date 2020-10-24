def calcula_pi(n):
    i=1
    pi=1
    while i<n and n>1:
        pi[i+1]=(pi[i]+(6/n**2))**(1/2)
        i+=1
        return pi