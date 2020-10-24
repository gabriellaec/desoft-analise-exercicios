def calcula_aumento(s):
    if s > 1250:
        return (s*1.10)-s
    else:
        return (s*1.15)-s

print("seu salario será {0:.0f}".format(calcula_aumento(500)))


