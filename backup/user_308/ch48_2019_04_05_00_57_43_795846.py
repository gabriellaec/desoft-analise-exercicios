mes=0
def num_mes(mes):
    mes=input("Qual o mês?: ")
    meses= ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
    for e in range(len(meses)):
        if meses[e]==mes:
            return e+1