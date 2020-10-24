from math import cos, radians
F = 10
theta = 0
S = 12
def calcula_trabalho (F, theta, s):
    trabalho = F* cos(radians(theta))*s
    return trabalho

print (calcula_trabalho(10, 0, 12))