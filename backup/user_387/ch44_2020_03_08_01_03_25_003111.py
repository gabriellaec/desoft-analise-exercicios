meses_do_ano = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro']

nome_do_mes = str(input('num do mes :'))


for mes in meses_do_ano:
    if mes == nome_do_mes:
        print((meses_do_ano.index(mes)) + 1)