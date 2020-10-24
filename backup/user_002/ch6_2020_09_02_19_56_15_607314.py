def celsius_para_fahrenheit(temperatura_celsius):
    temperatura_fahrenheit = (temperatura_celsius * 9/5) + 32
    return temperatura_fahrenheit

#Quanto é 100 graus Celsius em Fahrenheit?
celsius = 100
fahrenheit = celsius_para_fahrenheit(celsius)
print(fahrenheit)



