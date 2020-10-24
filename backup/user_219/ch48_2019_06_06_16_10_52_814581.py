mesescolhido= input(' Qual o nome do mês? ')
meses= ['janeiro' ,'fevereiro','março', 'abril','maio','junho','julho','agosto', 'setembro', 'outubro', 'novembro','dezembro']
contador= 1
for mes in meses:
    if mes != mesescolhido:
        contador+=1
    elif mes== mesescolhido:
        print(contador)
        

                    