import math
sin_x_bhaskara = (4*x*(180-x))/(40500-(x(180-x)))
sin_x_math =math.sin(x)

erro = abs(sin_x_bhaskara-sin_x_math)
print(erro)