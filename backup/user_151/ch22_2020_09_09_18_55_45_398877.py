def reduction(x, y):
    f = round((365 * x * y * 10) / (60 * 24), 0)
    return f

a = int(input('cigarros p/ dia '))
b = int(input('fuma a quantos anos '))

c = reduction(a, b)
print(c)