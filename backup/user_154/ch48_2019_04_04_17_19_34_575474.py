lista = ["", "Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]

def getNumber(string):
    result = 0
    for x in lista:
        if x.lower() == string.lower():
            break
        result = result + 1
    
    return result

print(getNumber(input("Número do mês"))