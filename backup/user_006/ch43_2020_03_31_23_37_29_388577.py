numero=int(input("Digite o numero do mes"))
meses=["janeiro", "fevereiro", "março", "abril", "maio" , "junho", "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"]
i=1
while i<13:
    if numero==i:
        print(meses[i])
    i=i+1