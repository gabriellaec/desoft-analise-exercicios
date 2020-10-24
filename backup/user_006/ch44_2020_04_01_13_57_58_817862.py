mes=input("Digite o nome de um mes:")
meses=["janeiro", "fevereiro", "março", "abril", "maio" , "junho", "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"]

i=0
while i<len(meses):
    if mes==meses[i]:
        print(i+1)
    i=i+1