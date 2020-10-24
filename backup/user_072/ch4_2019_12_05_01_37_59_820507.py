#def classifica_idade(x):
#    if x>17:
#    	return 'adulto' 
#    elif x<12:
#        return 'crianca'
#    else:
#        return 'adolescente'

def classifica_idade(x):
    if x<11:
        return 'crianca'
    elif x>=12 and x>=17:
        return 'adilescente'
    else:
        return 'adulto'