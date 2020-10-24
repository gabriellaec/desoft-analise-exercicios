def celsius_para_fahrenheit (x):
    y = 1.8*x+32
    return y 
#Temperatura em Celsius#
a = 55
b = celsius_para_farenheit (a)


print('{0} graus Celsius valem {1} graus Fahrenheit'.format(a, b))