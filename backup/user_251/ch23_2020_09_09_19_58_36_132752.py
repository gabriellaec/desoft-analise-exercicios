def limite_de_velocidade(a):
    if a > 80:
        return "você foi multado"
    else:
        return "você não foi multado"

def valor_da_multa(a):
   if a > 80:
       return (a-80)*5
    else:
        return 0
    


a = int(input("Qual foi sua velocidade? "))

print(limite_de_velocidade(a))
print(valor_da_multa(a))
