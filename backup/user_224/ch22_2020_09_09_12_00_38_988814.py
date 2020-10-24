def reduçao_da_vida_em_dias(cigarros_que_fuma_por_dia,numero_de_anos_que_fuma):
    reduçao_da_vida_em_dias = (1/144)*((cigarros_que_fuma_por_dia)*365*(numero_de_anos_que_fuma))
    return reduçao_da_vida_em_dias



num1=int(input('Digite a quantidade de cigarros que voce fuma por dia,aproximadamente'))
num2=int(input('Ha quantos anos você fuma?'))

z=(num1)*365
x = reduçao_da_vida_em_dias(num1,num2)

print('como sabemos que cada cigarro reduz seu tempo de vida em aproximadamente 10 minutos,a quantidade de dias que voce ira viver menos devido o uso de {0} cigarros por ano,é de {1} dia(s)'.format(z,x))
