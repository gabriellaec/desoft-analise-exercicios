def calcula_valor_devido(emp,mes,j):
    montante=emp*((1+j/100)**(mes))
    return montante
