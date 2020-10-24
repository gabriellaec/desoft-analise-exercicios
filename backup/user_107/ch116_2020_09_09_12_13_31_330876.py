def raiz_quadrada (valor):
    iterations = 1
    even = 1

    while valor > even:
      valor -= even
      iterations += 1
      even += 2

    return iterations