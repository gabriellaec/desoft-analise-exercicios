pergunta= float(input("Qual foi a sua velocidade?"))

def velocidade(número):
    valor_da_multa= (número-80)*5
    if número > 80:
        return 'Você foi multado R$ {0:.2f}' .format(valor_da_multa)
    if número <= 80:
        return "Não foi multado"
    
print (velocidade(pergunta))