mes=input("Digite o mês: ")
listanum=[1,2,3,4,5,6,7,8,9,10,11,12]
listanom=["Janeiro","Fevereiro","Março","Abril","Maio","Junho","Julho", "Agosto","Setembro","Outubro","Novembro","Dezembro"]
for i in listanom:
    if str(i)== mes:
        print(listanom[i])