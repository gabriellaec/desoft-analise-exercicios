def calcula_pi(n):
    if n==0:
        return "Digite um número válido."
    PI=0
    y=list(range(n))
    y.remove(0)
    for i in (y):
        PI+=(6/(i**2))
        x=i+1
    PI+=(6/(x**2))
    PI=(PI**(1/2))
    return PI