lista = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]

def getNumber(string):
    result = 1
    for x in lista:
        if x.lower() == string.lower():
            break
        result = result + 1
    return result

print(getNumber(input("Nome do mês"))