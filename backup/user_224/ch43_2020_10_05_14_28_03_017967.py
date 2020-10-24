numero_do_mes = int(input('Qual o numero do mes'))
lista_com_nome_dos_meses = ['mes_0','Janeiro','Fevereiro','Março','Abril','Maio','Junho','Julho','Agosto','Setembro','Outubro','Novembro','Dezembro']
i = 0 
while i < len(lista_com_nome_dos_meses) :
    if numero_do_mes == i :
        print(lista_com_nome_dos_meses[i])
    i += 1