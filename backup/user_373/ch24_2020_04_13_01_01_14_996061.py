salario= input('Salario atual: ')
def calcula_aumento (final):
    if salario > 1250:
        final= 1.1* salario
        return final
    else:
        final= 1.5* salario
        return final
        