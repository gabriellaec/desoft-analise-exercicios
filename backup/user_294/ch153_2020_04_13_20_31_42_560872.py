dicionario={'João': 10, 'Maria': 8, 'Miguel': 20, 'Helena': 67, 'Alice': 50}
def agrupa_por_idade(dicionario):
        crianca={}
        for i in dicionario:
            if dicionario[i]<=11:
                crianca[i]=["criança"]
            elif 12<=dicionario[i]<=17:
                crianca[i]=["adolescente"]
            elif 18<=dicionario[i]<=59:
                crianca[i]=["adulto"]
            else:
                crianca[i]=["idoso"]
        return crianca