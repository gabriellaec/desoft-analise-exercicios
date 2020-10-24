mês = ["janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"]
número = int(input("Qual o número do mês? "))
if 0<número<13:
    print (mês[número-1])
