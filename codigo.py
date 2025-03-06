import math

def calcular_fuerzas(masa, angulo, coef_frict, velocidad_inicial, tiempo, distancia=None, desde_arriba=True):
    """
    Calcula el peso, la fuerza normal, la fuerza de fricción, la fuerza neta,
    la aceleración, la velocidad final, el ángulo de inclinación y la distancia de la rampa.
    Ahora también considera el caso en que el objeto es lanzado hacia arriba.
    """
    # Convertir el ángulo de grados a radianes
    angulo_rad = math.radians(angulo)

    # Gravedad (m/s^2)
    g = 9.81

    # Calcular el peso del objeto
    peso = masa * g

    # Calcular las fuerzas
    W_paralelo = peso * math.sin(angulo_rad)  # Componente del peso paralelo al plano
    W_perpendicular = peso * math.cos(angulo_rad)  # Componente del peso perpendicular al plano
    N = W_perpendicular  # Fuerza normal
    F_friccion = coef_frict * N  # Fuerza de fricción

    # Determinar la dirección del movimiento
    if velocidad_inicial > 0 and not desde_arriba:
        # Movimiento hacia arriba en el plano
        F_neta = -W_paralelo - F_friccion  # La gravedad y la fricción se oponen al movimiento
    else:
        # Movimiento hacia abajo en el plano
        F_neta = W_paralelo - F_friccion

    # Aplicar la segunda ley de Newton
    aceleracion = F_neta / masa  # a = F/m

    # Caso especial: Si el objeto se mueve hacia arriba, determinar la distancia y tiempo hasta detenerse
    if velocidad_inicial > 0 and not desde_arriba:
        distancia = -(velocidad_inicial ** 2) / (2 * aceleracion)
        tiempo = -velocidad_inicial / aceleracion
        velocidad_final = 0  # Se detiene momentáneamente
    else:
        # Calcular la velocidad final
        velocidad_final = velocidad_inicial + aceleracion * tiempo

        # Calcular la distancia de la rampa si no se proporciona
        if distancia is None:
            distancia = velocidad_inicial * tiempo + 0.5 * aceleracion * tiempo**2

    # Ajustar la distancia según la dirección del lanzamiento
    if not desde_arriba:
        distancia = abs(distancia)

    # Retornar todos los resultados en un diccionario
    return {
        "Peso (N)": peso,
        "Fuerza Normal (N)": N,
        "Fuerza de Fricción (N)": F_friccion,
        "Fuerza Neta (N)": F_neta,
        "Aceleración (m/s^2)": aceleracion,
        "Velocidad Inicial (m/s)": velocidad_inicial,
        "Velocidad Final (m/s)": velocidad_final,
        "Distancia de la Rampa (m)": distancia,
        "Ángulo de Inclinación (grados)": angulo,
        "Tiempo (s)": tiempo
    }

# Función para solicitar datos al usuario
def obtener_datos():
    masa = float(input("Ingrese la masa del objeto (kg): "))
    angulo = float(input("Ingrese el ángulo del plano inclinado (grados): "))
    coef_frict = float(input("Ingrese el coeficiente de fricción: "))
    velocidad_inicial = float(input("Ingrese la velocidad inicial del objeto (m/s): "))
    tiempo = input("Ingrese el tiempo durante el cual se mueve el objeto (s) o presione Enter para calcularlo: ")
    distancia = input("Ingrese la distancia de la rampa (m) o presione Enter para calcularla: ")
    desde_arriba = input("¿El objeto se lanza desde arriba del plano inclinado? (s/n): ").strip().lower() == 's'
    
    return {
        "masa": masa,
        "angulo": angulo,
        "coef_frict": coef_frict,
        "velocidad_inicial": velocidad_inicial,
        "tiempo": float(tiempo) if tiempo else None,
        "distancia": float(distancia) if distancia else None,
        "desde_arriba": desde_arriba
    }

# Ejecutar el programa
datos = obtener_datos()

# Calcular las fuerzas y resultados
resultados = calcular_fuerzas(
    datos["masa"], datos["angulo"], datos["coef_frict"], datos["velocidad_inicial"],
    datos["tiempo"] if datos["tiempo"] is not None else 0, datos["distancia"], datos["desde_arriba"]
)

# Mostrar los resultados
print("\nResultados:")
for clave, valor in resultados.items():
    print(f"{clave}: {valor:.2f}")