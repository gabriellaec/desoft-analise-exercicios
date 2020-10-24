d = 1

termos = 1

maior = 1

resultado = 1

while d < 1000:

    a = d

    termos = 1

    while a != 1:

        if a % 2 == 0:

            a = a/2

            termos += 1

        else:

            a = 3*a + 1

            termos += 1

        if a == 1:

        if termos > maior:

        maior = termos

        resultado = d

        d += 1

        else:

        d += 1
print(resultado)