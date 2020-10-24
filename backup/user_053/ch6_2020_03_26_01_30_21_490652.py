def celsius_para_fahrenheit(C):
    F = (9*C)/5 + 32
    return F

temp_C = 25
temp_F = celsius_para_fahrenheit(temp_C)

print(temp_F)