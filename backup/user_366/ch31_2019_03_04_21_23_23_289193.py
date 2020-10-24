pergunta_casa = float(input('Qual o valor da casa?'));
pergunta_salario = float(input('Qual seu salário?'));
pergunta_tempo = float(input('Em quanto tempo, em anos, é para pagar?'));

a = pergunta_casa
b = pergunta_salario
c = pergunta_tempo

def prestacao(a, c):
    y = a/(c*12)
    return y

y = prestacao(a, c)

if y > 0.3*b:
    print("Empréstimo não aprovado");
else:
    print("Empréstimo aprovado");