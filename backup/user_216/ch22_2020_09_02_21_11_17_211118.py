cigarros = int(input("Número de cigarros"))
anos = int(input("Quanto tempo?"))

c = cigarros
a = anos

def f(a,c):
    y = 365 * a * c * 10
    return y

print(f(a,c))