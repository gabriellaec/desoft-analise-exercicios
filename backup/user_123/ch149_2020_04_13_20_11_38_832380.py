salbruto = float(input('Qual seu salário bruto?')
dep = int(input("quantos depented você tem?"))

if salbruto <= 1045:
    inss = salbruto - (salbruto*0.07) 
elif 1045 < salbruto <= 2089.60 :
    inss = salbruto - (salbruto*0.09)
elif 2089.61 < salbruto <= 3134.40 :
    inss = salbruto - (salbruto*0.12)
elif 3134.40 < salbruto <= 6101.06:
    inss = salbruto - (salbruto*0.14)

base_de_calculo = salbruto - inss - (dep * 189.59)

if base_de_calculo <= 1903.98:
    irrf = 0
elif 1903.98 < base_de_calculo <= 2826.65:
    irrf = (base_de_calculo*0.075)-142
elif 2826.65 < base_de_calculo <= 3751.05:
    irrf = (base_de_calculo*0.15)-354.80
elif 3751.05 < base_de_calculo <= 4664.68:
    irrf = (base_de_calculo*0.225)-636.13
else:
    irrf = (base_de_calculo*0.275)-869.36
print (irrf)
   