import math

g = 2.8  # [m/s²]

def calc_distance (speed, phi):
    sin_2_phi = math.sin(2 * phi)
    distance = speed**2 * sin_2_phi / g
    
    return distance

speed = float(input("Velocidade?"))
phi = float(input("Ânngulo de lançamento?"))

distance = calc_distance(speed, phi)

target_distance = distance - 100

if target_distance < -2:
    print("Muito perto")
elif target_distance > 2:
    print("Muito longe")
else:
    print("Acertou!")
