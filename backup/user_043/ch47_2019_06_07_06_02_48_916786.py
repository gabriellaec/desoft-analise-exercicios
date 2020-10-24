meses = {'1':'janeiro','2':'fevereiro','3':'marco','4':'abril','5':'maio','6':'junho','7':'julho','8':'agosto','9':'setembro','10':'outubro','11':'novembro','12':'dezembro'}
num = input('num mes: ')

def numero_mes(num):
    if num in meses:
        return meses[num]

numes = numero_mes(num)

print(numes)