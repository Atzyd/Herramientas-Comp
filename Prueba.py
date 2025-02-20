import math

def calcular_peso(masa):
    g = 9.8  
    return masa * g

def calcular_fuerza_normal(masa, angulo):
    g = 9.8
    F_g = calcular_peso(masa)
    theta = math.radians(angulo)
    F_perpendicular = F_g * math.cos(theta)
    return F_perpendicular

def calcular_fuerza_friccion(masa, angulo, coef_friccion):
    F_n = calcular_fuerza_normal(masa, angulo)
    return coef_friccion * F_n

def main():
    print("Seleccione qué desea calcular:")
    print("1. Peso")
    print("2. Fuerza Normal")
    print("3. Fuerza de Fricción")
    
    opcion = input("Ingrese el número de la opción deseada: ")

    try:
        masa = float(input("Ingrese la masa del objeto (kg): "))
        angulo = float(input("Ingrese el ángulo del plano inclinado (grados): "))

        if opcion == '1':
            peso = calcular_peso(masa)
            print(f"El peso del objeto es: {peso:.2f} N")
        
        elif opcion == '2':
            fuerza_normal = calcular_fuerza_normal(masa, angulo)
            print(f"La fuerza normal es: {fuerza_normal:.2f} N")
        
        elif opcion == '3':
            coef_friccion = float(input("Ingrese el coeficiente de fricción: "))
            fuerza_friccion = calcular_fuerza_friccion(masa, angulo, coef_friccion)
            print(f"La fuerza de fricción es: {fuerza_friccion:.2f} N")
        
        else:
            print("Opción no válida. Por favor, seleccione 1, 2 o 3.")

    except ValueError:
        print("Por favor, ingrese valores numéricos válidos.")

if __name__ == "__main__":
    main()