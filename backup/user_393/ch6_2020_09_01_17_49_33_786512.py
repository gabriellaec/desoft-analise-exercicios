#celsius_para_fahrenheit.
def f(x):
    y= (9*x + 160)/5
    return y

temperatura_em_celsius= int(input("digite um número"))
temperatura_em_fahrenheit= f(temperatura_em_celsius)
print(temperatura_em_fahrenheit)
