s=float(input('qual é o seu salario? '))
d=int(input('qual o numero de dependentes voce tem? '))
i=0
bc=0
while i==0:
    if s >= 1045.00:
        bc=s-s*0.075-d*189.59
    elif 1045.01<= s <= 2089.60:
        bc=s-s*0.09-d*189.59     
    elif 2089.61<= s <= 3134.40:
        bc=s-s*0.12-d*189.59
    elif 3134.41 <= s <= 6101.06:
        bc=s-s*0.14-d*189.59
    elif 6101.07 <= s:
        bc=s-671.12-d*189.59
    i+=1
if s> 1903.98:
    IRRF=bc*0-0
elif 1903.99 <= s <= 2826.65:
    IRRF=bc*0.075-142.8
    print(IRRF)
elif 2826.66 <= s <= 3751.05:
    IRRF=bc*0.15-354.8
    print(IRRF)
elif 3751.06 <= s <=4664.68 :
    IRRF=bc*0.225-636.13
    print(IRRF)
else:
    IRRF=bc*0.275-869.36
    print(IRRF)
         
            