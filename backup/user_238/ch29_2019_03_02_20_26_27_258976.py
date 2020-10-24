def aumento(salario):
        if salario > 1250:
            resultado = (1.1*salario) - salario
        elif salario <= 1250:
            resultado = (1.15*salario) - salario
        return resultado

print (aumento(1300))