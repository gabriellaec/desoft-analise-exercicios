def calcula_aumento(s):
    if s > 1250:
        return s*1.1
    else:
        return s*1.15

print(calcula_aumento(1250))
print(calcula_aumento(2500))
