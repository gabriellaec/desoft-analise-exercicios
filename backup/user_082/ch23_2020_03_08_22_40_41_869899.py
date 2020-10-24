velocidade_do_carro= int(input('Qual a velocidade do carro? '))
if velocidade_do_carro <= 80:
    print ('Não foi multado')
elif velocidade_do_carro >= 80:
    pagar= (velocidade_do_carro - 80)*5
    print (f'Voce foi multado e deve pagar R${pagar:.2f}')