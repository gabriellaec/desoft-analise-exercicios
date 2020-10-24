def celsius_para_fahrenheit(F):
    C = (F-32)*5/9
    return C

fahrenheit = 100
celsius = celsius_para_fahrenheit(fahrenheit)
print (celsius)