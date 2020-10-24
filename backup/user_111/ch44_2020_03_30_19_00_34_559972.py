i=int(input("Digite o nome do mês: "))
numero_do_mes=[1,2,3,4,5,6,7,8,9,10,11,12]
nome_do_mes=["janeiro","fevereiro","março","abril","maio","junho","julho","agosto","setembro","outubro","novembro","dezembro"]
numero_do_mes[i-1]=nome_do_mes[i-1]
print(numero_do_mes[i-1])