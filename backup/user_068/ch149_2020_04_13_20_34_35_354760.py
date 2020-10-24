a = float(input("Qual salário bruto?"))
b = int(input("Qual o número de dependentes do usuário?"))
if a < 1045.01:
    aliquota = 0.075
    contribuicao = a* aliquota
    base = a - contribuicao - b*189.59
    if base < 1903.99:
        irrf = 0
    if base> 1903.98 and base<2826.66:
        irrf = base* 0.075 - 142.80
    if base > 2826.65 and base< 3751.06:
        irrf = base*0.015 - 354.80
    if base> 3751.05 and base<4664.69:
        irrf = base*0.225 - 636.13
    if base > 4664.68:
        irrf = base* 0.275-869.36
if a> 1045 and a< 2089.60:
    aliquota = 0.09
    contribuicao = a* aliquota
    base = a - contribuicao - b*189.59
    if base < 1903.98:
        irrf = 0
    if base> 1903.98 and base<2826.66:
        irrf = base* 0.075 - 142.80
    if base > 2826.65 and base< 3751.06:
        irrf = base*0.015 - 354.80
    if base> 3751.05 and base<4664.69:
        irrf = base*0.225 - 636.13
    if base > 4664.68:
        irrf = base* 0.275-869.36
if a > 2089.60 and a< 3751.06:
    aliquota = 0.12
    contribuicao = a* aliquota
    base = a - contribuicao - b*189.59
    if base < 1903.98:
        irrf = 0
    if base> 1903.98 and base<2826.66:
        irrf = base* 0.075 - 142.80
    if base > 2826.65 and base< 3751.06:
        irrf = base*0.015 - 354.80
    if base> 3751.05 and base<4664.69:
        irrf = base*0.225 - 636.13
    if base > 4664.68:
        irrf = base* 0.275-869.36
if a > 3134.40 and a< 6101.06:
    aliquota = 0.14
    contribuicao = a* aliquota
    base = a - contribuicao - b*189.59
    if base < 1903.98:
        irrf = 0
    if base> 1903.98 and base<2826.66:
        irrf = base* 0.075 - 142.80
    if base > 2826.65 and base< 3751.06:
        irrf = base*0.015 - 354.80
    if base> 3751.05 and base<4664.69:
        irrf = base*0.225 - 636.13
    if base > 4664.68:
        irrf = base* 0.275-869.36
if a>6101.06:
    base = a -  671.12 - b*189.59
    if base < 1903.98:
        irrf = 0
    if base> 1903.98 and base<2826.66:
        irrf = base* 0.075 - 142.80
    if base > 2826.65 and base< 3751.06:
        irrf = base*0.015 - 354.80
    if base> 3751.05 and base<4664.69:
        irrf = base*0.225 - 636.13
    if base > 4664.68:
        irrf = base* 0.275-869.36

print(irrf)
    