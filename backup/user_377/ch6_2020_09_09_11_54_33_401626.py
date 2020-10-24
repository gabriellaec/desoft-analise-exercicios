# função que converte celsius para fahrenheit
def celsius_para_fahrenheit(valor_celsius):
    valor_fahrenheit = valor_celsius*1.8 + 32
    return valor_fahrenheit

# quanto que é 30 celsius em fahrenheit
celsius = 30
fahrenheit = celsius_para_fahrenheit(celsius)
print (fahrenheit)   