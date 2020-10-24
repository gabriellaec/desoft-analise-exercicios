def celsius_para_fahrenheit(c):
    f= (c*9/5)+32
    return f
c=int(input('digite a temperatura em celsius'))
d=celsius_para_fahrenheit(c)
print(d)