dict_numero_dia = {
"domingo": 1,
"segunda": 2,
"terça": 3,
"quarta": 4,
"quinta": 5,
"sexta": 6,
"sábado": 7
}
nome_dia = input("Digite o nome do dia da semana: ")
if nome_dia in dict_numero_dia:
numero_dia = dict_numero_dia[nome_dia]
print("{0} é o dia número {1}".format(nome_dia, numero_dia))
else:
print("Esse dia não existe!")
    
    
    