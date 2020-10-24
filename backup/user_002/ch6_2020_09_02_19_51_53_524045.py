#Função que converte temperatura em Celsius para Fahrenheit

def celsius_para_fahrenheit(temperatura_celsius):
    temperatura_fahrenheit = 1.8 * temperatura_celsius
    return temperatura_fahrenheit

#Quanto é 100 graus Celsius em Fahrenheit?
celsius = 100
fahrenheit = celsius_para_fahrenheit(celsius)
print(fahrenheit)


