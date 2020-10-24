numero_do_mes = input('Qual o mes?')
lista_com_nome_dos_meses = ['mes_0','Janeiro','Fevereiro','Março','Abril','Maio','Junho','Julho','Agosto','Setembro','Outubro','Novembro','Dezembro']
lista_numero_do_mes = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
i = 0
while i < len(lista_com_nome_dos_meses) - 1 :
    if numero_do_mes == lista_numero_do_mes[i] :
        print(lista_com_nome_dos_meses[i])
        i += 1