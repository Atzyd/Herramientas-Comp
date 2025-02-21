#es una biblioteca estandarizada en Python que brinda acceso a funciones y constantes matemáticas
import math
#Definiendo cada variable
#Cada "return" significa enviar un valor de vuelta a la parte del programa que llamó a la función
def CP4(RACH2):
    GR1 = 9.8
    return RACH2 * GR1

def CF2(RACH2, ATZ7):
    GR1 = 9.8
    FG = CP4(RACH2)
    TH1 = math.radians(ATZ7)
    FP2 = FG * math.cos(TH1)
    return FP2

def FRE3(RACH2, ATZ7,  CF01):
    HHK2 = CF2(RACH2, ATZ7)
    return  CF01 * HHK2

def HOD9(RACH2, ATZ7,  CF01):
    FG = CP4(RACH2)
    FP2 = FG * math.sin(math.radians(ATZ7))
    FO2 = FRE3(RACH2, ATZ7,  CF01)
    return FP2 - FO2

def CA4(RACH2, ATZ7,  CF01):
    FOR3 = HOD9(RACH2, ATZ7,  CF01)
    return FOR3 / RACH2
#Inicio del menu
def main():
    print("Seleccione qué desea calcular:")
    print("1. Peso")
    print("2. Fuerza Normal")
    print("3. Fuerza de Fricción")
    print("4. Fuerza Neta")
    print("5. Aceleración")
    #Aclaracion cada "input" es una solicitud al usuario para llevar a cabo el funcionamiento del algoritmo
    opcion = input("Ingrese el número de la opción deseada: ")
    # ".2f" indica el inicio del especificador de formato
    try:
        if opcion == '1':
            RACH2 = float(input("Ingrese la masa del objeto (kg): "))
            PS02 = CP4(RACH2)
            print(f"El peso del objeto es: {PS02:.2f} N")
        
        elif opcion == '2':
            RACH2 = float(input("Ingrese la masa del objeto (kg): "))
            ATZ7 = float(input("Ingrese el ángulo del plano inclinado (grados): "))
            IL23 = CF2 (RACH2, ATZ7)
            print(f"La fuerza normal es: {IL23:.2f} N")
        
        elif opcion == '3':
            RACH2 = float(input("Ingrese la masa del objeto (kg): "))
            ATZ7 = float(input("Ingrese el ángulo del plano inclinado (grados): "))
            CF01 = float(input("Ingrese el coeficiente de fricción: "))
            KOL5 = FRE3(RACH2, ATZ7,  CF01)
            print(f"La fuerza de fricción es: {KOL5:.2f} N")
        
        elif opcion == '4':
            RACH2 = float(input("Ingrese la masa del objeto (kg): "))
            ATZ7 = float(input("Ingrese el ángulo del plano inclinado (grados): "))
            CF01 = float(input("Ingrese el coeficiente de fricción: "))
            FN23 = HOD9 (RACH2, ATZ7,  CF01)
            print(f"La fuerza neta es: {FN23:.2f} N")
        
        elif opcion == '5':
            RACH2 = float(input("Ingrese la masa del objeto (kg): "))
            ATZ7 = float(input("Ingrese el ángulo del plano inclinado (grados): "))
            CF01 = float(input("Ingrese el coeficiente de fricción: "))
            AC34 = CA4(RACH2, ATZ7,  CF01)
            print(f"La aceleración del objeto es: {AC34:.2f} m/s^2")
        
        else:
            print("Opción no válida. Por favor, seleccione un número del 1 al 5.")
#Si es ingresado algun dato no identificado el "except" va a arrojar el mensaje dicho anteriormente
    except ValueError:
        print("Por favor, ingrese valores numéricos válidos.")

if __name__ == "__main__":
    main()