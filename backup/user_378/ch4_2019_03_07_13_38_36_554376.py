def classifica_idade(x):
    if x<=11:
      return 'crianca'
    elif x>=12 and x<18:
      return 'adolescente'
    else:
      return 'adulto'