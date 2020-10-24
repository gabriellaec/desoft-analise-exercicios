def celsius_para_fahrenheit (c):
    y = (9*c)/5 + 32
    return y
valor_celsius = int (input (print ("Fale um valor em celsius:")))
valor_fahrenheit = celsius_para_fahrenheit(valor_celsius)
print ("{}ºC em Fahrenheit vale {}ºF." .format (valor_celsius,valor_fahrenheit))