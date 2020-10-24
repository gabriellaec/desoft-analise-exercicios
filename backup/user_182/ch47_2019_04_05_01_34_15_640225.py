meses=[0]*12
meses=["janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"]

n=int(input("qual o número do mes"))
while n<1 or n>12:
    print('inválido')
    n=int(input("qual o número do mes"))
pos =n-1
print(meses[pos])