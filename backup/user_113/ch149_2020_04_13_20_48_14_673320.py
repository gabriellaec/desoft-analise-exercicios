salario= float(input("Qual o seu salário bruto?: "))
num_depend= float(input("Qual seu número de dependentes?: "))

if salario<=float("1.045,00"):
    aliq=0.075
    contri= int(0.075*salario)
    
elif "1.045,01"<=salario<="2.089,60":
    aliq=0.09
    contri= int(0.09 * salario)
    
elif salario>="2.089,61" or salario<="3.134,40":
    aliq=0.12
    contri= int(0.12 * salario)
    
elif "3.134,41"<=salario<="6.101,06":
    aliq=0.14
    contri= int(0.14 * salario)
    
elif salario>"6.101,06":
    aliq= 671,12
    contri= 671,12
    
base_de_cal= int (salario - contri - (num_depend*189,59))


if base_de_cal<="1.903,98":
    aliq2=0.0
    ded= 0,00
    
elif "1.903,99"<=base_de_cal<="2.826,65":
    aliq2=0.075
    ded=142,80
    
elif "2.826,66"<=base_de_cal<="3.751,05":
    aliq2=0.15
    ded=354,80
    
elif "3.751,06"<=base_de_cal<="4.664,68":
    aliq2=0.225
    ded=636,13
    
elif base_de_cal>"4.664,68":
    aliq2=0.275
    ded=869,36

IRRF = int((base_de_cal * aliq2) - ded )