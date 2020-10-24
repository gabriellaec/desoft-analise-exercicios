def collatz(numero):
    if numero == 1:
        return
    if numero % 2 == 0:
        collatz(numero / 2)
    else:
        collatz(3 * numero + 1)

collatz(50)
print(collatz)