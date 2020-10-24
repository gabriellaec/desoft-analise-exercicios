def remove_vogais(palavra):
    vogais= 'aeiou'
    palavra_sem_vogais= [k for k in palavra if k not in vogais]
    soma= ''
    i= 0
    while i < len(palavra_sem_vogais):
        soma= soma + palavra_sem_vogais[i]
        i= i + 1
    return soma
