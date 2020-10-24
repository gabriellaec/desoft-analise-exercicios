def Aprovar_emprestimo(v, s, a):
    if v/(a*12) > s*0.3:
        return'Empréstimo não aprovado'
    else:
        return'Empréstimo aprovado'

w= int(input('valor da casa '))
q= int(input('salário '))
e= int(input('quantos anos '))

print (Aprovar_emprestimo(w, q, e))