def classifica_idade(idade):
    idade = int(input('Qual a sua idade'))
        
        if idade <= 11:
           return 'crianca'
        else:
           if idade <= 17:
              return 'adolecente'
           else:
              return 'adulto'