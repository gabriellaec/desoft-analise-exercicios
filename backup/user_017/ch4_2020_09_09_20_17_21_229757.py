def classifica_idade(x):
    if x <= 11:
     return str("crianca")
   
    elif 12 <= x <= 18:
     return str("adolecente")
   
    else:
     return str("adulto")
x=20
a= classifica_idade(x)
print(a)

