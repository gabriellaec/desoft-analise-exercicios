def primos_entre(intervalo):
    import math #Ideia é não fazer a função depender de nada de fora dela, então importo dentro
    def is_prime(number): # Definindo a função auxiliar dentro da função de interesse
        if number > 1:
            if number == 2:
                return True
            if number % 2 == 0:
                return False
            for current in range(3, int(math.sqrt(number) + 1), 2): # step = 2 => busca só nos ímpares
                if number % current == 0: 
                    return False
            return True
        return False
    primos = [primo for primo in list(range(intervalo)) #List comprehension; veja que já crio a lista com os elementos no intervalo aqui
                if is_prime(primo)]  # No Python, está subentendido que a condição é 'if is_prime() == True'
    return primos

if __name__ == '__main__':
    print(achar_primos(1000))