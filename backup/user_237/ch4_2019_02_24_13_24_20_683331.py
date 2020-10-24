 def classifica_idade(idade):
        if idade < 12:
            return str("crianca")
        if idade > 12 and idade < 18:
            return str("adolescente")
        else:
            return str("adulto")