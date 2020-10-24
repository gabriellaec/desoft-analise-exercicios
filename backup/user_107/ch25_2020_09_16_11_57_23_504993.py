import math

g = 9.8  # [m/s²]

def calc_distance (speed, theta):
    sin_2_theta = math.sin(2 * theta)
    speed_squared = speed ** 2
    distance = speed_squared * sin_2_theta / g
    
    return distance

speed = float(input("Velocidade?"))
theta = float(input("Ângulo de lançamento?"))

distance = calc_distance(speed, theta)
target_distance = distance - 100

if target_distance < -2:
    print("Muito perto")
elif target_distance > 2:
    print("Muito longe")
else:
    print("Acertou!")
