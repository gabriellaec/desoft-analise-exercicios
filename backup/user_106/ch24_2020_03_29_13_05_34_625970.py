def calcula_aumento(s):
    if s>1250:
        x=s*1.10
        return x
    else:
        x=s*1.15
        return x

print(calcula_salario(1000))
print(calcula_salario(1250))
print(calcula_salario(2000))