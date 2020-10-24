import math 

erro = []
for θ in range(91):
    bsk = 4 * θ * (180 - θ)/(40500 - θ * (180 - θ))
    mat = math.sin(math.radians(θ))
    erro.append(abs(bsk-mat))

print(max(erro))