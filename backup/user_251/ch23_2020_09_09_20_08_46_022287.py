def limite_de_velocidade(a):
    if a > 80:
        return "você foi multado e o valor de sua multa é: {0}".format(valor_da_multa(a))
    else:
        return "Não foi multado"

def valor_da_multa(a):
   if a > 80:
        return (a-80)*5
    
a = int(input("Qual foi sua velocidade? "))

print(limite_de_velocidade(a))




