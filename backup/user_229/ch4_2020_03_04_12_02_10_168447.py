def classifica_idade(idade):
    if int(idade<12):
        print("criança")
    if int(11<idade<18):
        print("adolescente")
    if int(idade>17):
        print("adulto")
    