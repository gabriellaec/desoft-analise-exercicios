idade = int(input('coloque sua idade:'))
def classifica_idade(idade):
    if idade<=11 :
        return 'criança'
    elif 12 <= idade <= 17:
        return 'adolescente'        
    else:
        return 'adulto' 
    print(classifica_idade(idade))     