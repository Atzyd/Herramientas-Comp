#Libreria para los calculos matematicos-Ejemplo convertir grados a radianes y calcular las funciones trigonometricas
import math

def calcular_fuerzas(masa=None, angulo=None, coef_frict=None, velocidad_inicial=None, velocidad_final=None, tiempo=None, distancia=None, desde_arriba=True):
    """
    Calcula todas las fuerzas y parámetros en un plano inclinado.
    """
    g = 9.8  # Gravedad (m/s^2)
    if angulo is None:
        raise ValueError("El ángulo del plano inclinado es obligatorio para los cálculos.")
    
    #Cambio de angulos a radianes
    angulo_rad = math.radians(angulo)
    
    # Calcular peso y sus componentes si se conoce la masa
    if masa is not None:
        peso = masa * g
        W_paralelo = peso * math.sin(angulo_rad)
        W_perpendicular = peso * math.cos(angulo_rad)
        N = W_perpendicular  # Fuerza normal
    else:
        peso = W_paralelo = W_perpendicular = N = None
    
    # Calcular fuerza de fricción si hay coeficiente de fricción y la fuerza normal está definida
    F_friccion = 0
    if coef_frict is not None and N is not None:
        F_friccion = coef_frict * N
    
    # Depende de la direccion se arroja el signo negativo o posivo:)
    direccion = -1 if velocidad_inicial and velocidad_inicial > 0 and not desde_arriba else 1
    
    # Calcular aceleración considerando la fricción
    if masa is not None:
        # Si se proporciona la masa, calculamos la aceleración considerando la fricción
        aceleracion = -g * (math.sin(angulo_rad) + coef_frict * math.cos(angulo_rad))  # Se asegura de restar correctamente la fricción
    else:
        # Si no se proporciona la masa, solo depende de la gravedad y el ángulo, sin fricción
        aceleracion = -g * math.sin(angulo_rad)
    
    # Calcular distancia si no se proporciona
    if distancia is None and velocidad_inicial is not None and velocidad_final is not None:
        if aceleracion != 0:
            distancia = (velocidad_final**2 - velocidad_inicial**2) / (2 * aceleracion)
        else:
            distancia = 0
    
    # Calcular tiempo si no se proporciona
    if tiempo is None and velocidad_inicial is not None and velocidad_final is not None:
        if aceleracion != 0:
            
            tiempo = abs(velocidad_inicial / (g * (math.sin(angulo_rad) + coef_frict * math.cos(angulo_rad))))
    
    # Calcular fuerza neta
    F_neta = W_paralelo - F_friccion  

    # Calcular cambio de energía cinética
    if masa is not None and velocidad_inicial is not None and velocidad_final is not None:
        energia_cinetica_inicial = 0.5 * masa * velocidad_inicial**2
        energia_cinetica_final = 0.5 * masa * velocidad_final**2
        cambio_energia_cinetica = energia_cinetica_final - energia_cinetica_inicial
    else:
        cambio_energia_cinetica = None
    
    # Calcular cambio de energía potencial
    if masa is not None and distancia is not None:
        cambio_energia_potencial = masa * g * distancia * math.sin(angulo_rad)
    else:
        cambio_energia_potencial = None
    
    return {
        "Masa (kg)": masa,
        "Peso (N)": peso,
        "Fuerza Normal (N)": N,
        "Fuerza de Fricción (N)": F_friccion,
        "Fuerza Neta (N)": F_neta,
        "Coeficiente de Fricción": coef_frict,
        "Aceleración (m/s^2)": aceleracion,
        "Velocidad Inicial (m/s)": velocidad_inicial,
        "Velocidad Final (m/s)": velocidad_final,
        "Distancia Recorrida (m)": distancia,
        "Ángulo de Inclinación (grados)": angulo,
        "Tiempo (s)": tiempo,
        "Cambio de Energía Cinética (J)": cambio_energia_cinetica,
        "Cambio de Energía Potencial (J)": cambio_energia_potencial
    }
#Ingreso de datos Y manejo de errores :))))
def obtener_datos():
    def leer_float(mensaje):
        while True:
            try:
                valor = input(mensaje).strip()
                if valor == "":
                    return None
                return float(valor)
            except ValueError:
                print("Entrada no válida. Por favor, ingrese un número válido.")

    return {
        "masa": leer_float("Ingrese la masa del objeto (kg) o presione Enter si no la conoce: "),
        "angulo": leer_float("Ingrese el ángulo del plano inclinado (grados): "),
        "coef_frict": leer_float("Ingrese el coeficiente de fricción o presione Enter para calcularlo: "),
        "velocidad_inicial": leer_float("Ingrese la velocidad inicial del objeto (m/s) o presione Enter si no la conoce: "),
        "velocidad_final": leer_float("Ingrese la velocidad final del objeto (m/s) o presione Enter si no la conoce: "),
        "tiempo": leer_float("Ingrese el tiempo de movimiento (s) o presione Enter para calcularlo: "),
        "distancia": leer_float("Ingrese la distancia recorrida en la rampa (m) o presione Enter para calcularla: "),
        "desde_arriba": input("¿El objeto se lanza desde arriba del plano inclinado? (s/n): ").strip().lower() == 's'
    }

if __name__ == "__main__":
    try:
        datos = obtener_datos()
        
        # Calcular las fuerzas y resultados
        resultados = calcular_fuerzas(
            datos["masa"],
            datos["angulo"],
            datos["coef_frict"],
            datos["velocidad_inicial"],
            datos["velocidad_final"],
            datos["tiempo"],
            datos["distancia"],
            datos["desde_arriba"]
        )
        
        # Mostrar los resultados
        print("\nResultados:")
        for clave, valor in resultados.items():
            print(f"{clave}: {valor:.2f}" if isinstance(valor, (int, float)) else f"{clave}: No calculado")
    except Exception as e:
        print(f"Se produjo un error: {e}")
