idade = int(input('coloque sua idade:'))
def classifica_idade(idade):
    if idade<=11 :
        return 'crianca'
    elif 12 <= idade or idade <= 17:
        return 'adolescente'        
    else:
        return 'adulto' 
