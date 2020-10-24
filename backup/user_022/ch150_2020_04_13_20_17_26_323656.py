def calcula_pi(t):
    if t==0:
        return "Digite um número válido."
    PI=0
    x=list(range(t))
    x.remove(0)
    for i in (x):
        PI+=(6/(i**2))
    z+=1
    PI+=(6/(z**2))
    PI=(PI**(1/2))
    return PI