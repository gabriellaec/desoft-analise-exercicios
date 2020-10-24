 def classifica_idade(idade):
        if idade < 12:
            return str("crianca")
        if 12 < idade and idade < 18:
            return str("adolescente")
        else:
            return("adulto")