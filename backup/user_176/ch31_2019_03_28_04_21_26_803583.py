vc= float(input('qual o valor da casa? '))
sal= float(input('qual o salario? '))
t= int(input('em quantos anos vai pagar? '))
meses= t*12
vp= vc/meses
if vp > 0.3*sal:
    print('Empréstimo não aprovado')
else:
    print('Empréstimo aprovado')