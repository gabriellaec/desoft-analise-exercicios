def calcula_aumento(salary):
    new_salary = salary
    
    if salary <= 1250:
        new_salary *= 15/100
    else:
        new_salary *= 10/100
        
    return new_salary