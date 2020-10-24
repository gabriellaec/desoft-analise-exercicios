meses = ["Janeiro","Fevereiro","Março","Abril","Maio","Junho","Julho","Agosto","Setembro","Outubro","Novembro","Dezembro"]
nome_do_mes = int(input("Digite o nome do mes: "))
while not  nome_do_mes in meses:
    print("Invalido")
    nome_do_mes = input("Digite o nome do mes: ")
i = 0
while i <len(meses):
    if nome_do_mes == meses[i]:
        print(i+1)
        break
    i += 1
    
    
    
    
    