def classifica_idade(age):
    if age >= 18:
        print("adulto")
    elif age >= 12 and age <= 17:
        print("adolescente")
    else:
        print("crianca")