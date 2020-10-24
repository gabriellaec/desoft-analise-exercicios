def calcula_pi(t):
    if t==0:
        return "Digite um número válido."
    pi=0
    x=list(range(t))
    x.remove(0)
    for i in (x):
        pi+=(6/(i**2))
    pi=(pi**(0.5))
    return pi