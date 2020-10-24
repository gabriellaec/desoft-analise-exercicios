lista = ["Janeiro", "Fevereiro", "Marco", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]

def getNumber(string):
    result = 1
    for x in lista:
        if x == string:
            break
        result = result + 1
    return result

print(getNumber(input("Nome do mês"))