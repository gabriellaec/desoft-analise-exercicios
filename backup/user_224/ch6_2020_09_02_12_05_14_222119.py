#converter graus celsius em fharenheit
def celsius_para_fharenheit(x):
    temperatura_em_fharenheit = ((temperatura_em_celsius*9/5)+32)
    return temperatura_em_fharenheit

#converter 40 graus celsius em fharenheit
temperatura_em_celsius = 40
temperatura_em_fharenheit = celsius_para_fharenheit(temperatura_em_celsius)
print (temperatura_em_fharenheit)