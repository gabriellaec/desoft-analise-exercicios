def celsius_para_fahrenheit(temperatura_celcius):
    temperatura_fahrenheit = temperatura_celcius*1.8+32
    print("A temperatura em Fahrenheit é: {0}".format(temperatura_fahrenheit))
t = float(input("Qual a temperatura em celsius: "))
celsius_para_fahrenheit(t)