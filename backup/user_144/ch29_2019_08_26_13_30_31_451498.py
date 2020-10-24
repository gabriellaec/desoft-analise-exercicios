salario = float(input("Digite seu salário: "))
pc_aumento = 0.10
pc_aumento2 = 0.15

def calcula_aumento(salario):
    if salario >=1250:
        aumento = salario * pc_aumento
    if salario <=1250:
        aumento = salario * pc_aumento2
        
        return aumento 
        
        
  