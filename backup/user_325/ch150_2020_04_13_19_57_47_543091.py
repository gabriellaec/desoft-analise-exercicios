def calcula_pi(n):
    if n==0:
        return "Digite um número válido."
    pi=0
    ran=list(range(n))
    ran.remove(0)
    for i in (ran):
        pi+=(6/(i**2))
    pi=(pi**(1/2))
    return pi