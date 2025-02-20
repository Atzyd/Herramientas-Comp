import math

def calcular_aceleracion(masa, angulo, coef_friccion):
    g = 9.81  # m/s^2

    theta = math.radians(angulo)

    F_g = masa * g

    F_paralela = F_g * math.sin(theta)
    F_perpendicular = F_g * math.cos(theta)

    F_n = F_perpendicular

    F_f = coef_friccion * F_n

    F_neto = F_paralela - F_f

    if masa > 0:
        aceleracion = F_neto / masa
    else:
        aceleracion = 0

    return aceleracion

try:
    masa = float(input("Ingrese la masa del objeto (kg): "))
    angulo = float(input("Ingrese el ángulo del plano inclinado (grados): "))
    coef_friccion = float(input("Ingrese el coeficiente de fricción: "))

    aceleracion = calcular_aceleracion(masa, angulo, coef_friccion)
    print(f"La aceleración del objeto en el plano inclinado es: {aceleracion:.2f} m/s²")

except ValueError:
    print("Por favor, ingrese valores numéricos válidos.")