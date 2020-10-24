num_cigarros=int(input("quantos cigarros você fuma por dia?"))
num_anos=int(input("fazem quantos anos que você fuma?"))
def f(x,z):
    y=(x/144)*365*z
    return y

e=f(num_anos,num_cigarros)
print("{0:.2f} dias" .format(e))
