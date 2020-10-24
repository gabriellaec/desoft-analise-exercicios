def celsius_para_fahrenheit(x):
    y= 1.8 * x +32
    return y
Temperatura = int(input('digite a temperatura em Celsius'))
resultado = celsius_para_fahrenheit(Temperatura)
print(resultado)