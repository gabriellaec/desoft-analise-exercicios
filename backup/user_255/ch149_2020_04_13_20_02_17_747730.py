s=int(input('Qual o seu salario bruto?   '))
d=int(input('Qual o numero de dependentes?   '))
if s<=1045:
    def inss(s):
        i=0.075*s
        return i
elif s>=1045.01 and s<=2089.60:
    def inss(s):
        i=0.09*s
        return i
    i=inss(s)
elif s>=2089.61 and s<=3134.40:
    def inss(s):
        i=0.12*s
        return i
    i=inss(s)
elif s>=3134.41 and s<=6101.06:  
    def inss(s):
        i=0.14*s
        return i
    i=inss(s)
elif s>=6101.07:
    def inss(s):
        i=671.12
        return i
    i=inss(s)
#base de calculo irrf#
def base_de_calculo_irrf(s,i,d):
    b=s-i-d*189.59
    return b
b=base_de_calculo_irrf(s,i,d)
#irrf simplificado#
if b<=1903.98:
    def irrf_simplificado(b):
        r=0
        return r
    r=irrf_simplificado(b)
    
elif b>=1903.99 and b<=2826.65:
    def irrf_simplificado(b):
        r=b*0.075-142.80
        return r 
    r=irrf_simplificado(b)
    
elif b>=2826.66 and b<=3751.05:
    def irrf_simplificado(b):
        r=b*0.15-354.80
        return r 
    r=irrf_simplificado(b)
    
elif b>=3751.06 and b<=4664.68:
    def irrf_simplificado(b):
        r=b*0.225-636.13
        return r 
    r=irrf_simplificado(b)
elif b>=4664.69:
    def irrf_simplificado(b):
        r=b*0.275-869.36
        return r 
    r=irrf_simplificado(b)
print ('O seu IRRF simplificado é:')
print (r)
