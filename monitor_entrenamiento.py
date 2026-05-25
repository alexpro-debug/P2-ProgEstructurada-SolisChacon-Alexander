""" 
Nombre del Alumno: Alexander Solis Chacon 
Matrícula: UX25II153 
Fecha: 25/05/2026 
Examen Segundo Parcial - Programación Estructurada 
""" 
# ========================================== 
# 1. IMPORTACIÓN DE BIBLIOTECAS ESTÁNDAR 
# ========================================== 
import datetime 
import math 
import random 
import statistics 
import sys 
# ========================================== 
# 2. DEFINICIÓN DE CONSTANTES 
# ========================================== 
MAX_EPOCHS = 10 
UMBRAL_ERROR_CRITICO = 0.95 
# ========================================== 
# 3. FUNCIONES DEFINIDAS POR EL USUARIO 
# ========================================== 
def obtener_info_sistema(): 
    """ 
    Usa la biblioteca 'sys' para validar el entorno de ejecución. 
    Requisitos: Realizar 3 llamadas distintas a la biblioteca 'sys'. 
    """ 
    #1. sys.platform: mostrar información de la plataforma
    plataforma = sys.platform
    #2. sys.version: verificar la versión de Python
    version = sys.version
    
    print("--- Información del Entorno ---")
    print(f"Sistema Operativo: {plataforma}")
    print(f"Versión de Python: {version}")
    print("-------------------------------\n")
    return plataforma

def simular_metricas_entrenamiento(cantidad_epochs): 
    """ 
    Usa las bibliotecas 'random' y 'datetime' para simular los datos de entrenamiento. 
    Requisitos: 3 llamadas a 'random' y 3 llamadas a 'datetime'. 
    """ 
    #1. datetime.datetime.now(): hora de inicio
    tiempo_inicio = datetime.datetime.now()
    #2. strftime(): formatear la fecha en español
    print(f"Inicio del entrenamiento: {tiempo_inicio.strftime('%d/%m/%Y %H:%M:%S')}")

    lista_loss = []
    latencias = []
    eventos = ["Epoch exitoso", "Gradiente inestable", "Actualización de pesos"]

    for i in range(cantidad_epochs):
        #1. random.random(): generar fluctuación del error de pérdida
        loss = random.random() 
        #2. random.uniform(): simular probabilidad/latencia en segundos
        latencia = random.uniform(0.1, 1.2)
        #3. random.choice(): seleccionar evento aleatorio
        evento_log = random.choice(eventos)

        lista_loss.append(loss)
        latencias.append(latencia)
        print(f"Epoch {i+1}/{cantidad_epochs} - Loss: {loss:.4f} - Evento: {evento_log}")

    #3. resta de objetos datetime para obtener diferencia simulada
    tiempo_fin = datetime.datetime.now()
    diferencia_tiempo = tiempo_fin - tiempo_inicio
    print(f"Fin del entrenamiento. Tiempo transcurrido: {diferencia_tiempo.total_seconds()} segundos.\n")

    return lista_loss, latencias

def analizar_rendimiento(lista_loss, latencias): 
    """ 
    Usa la biblioteca 'statistics' para analizar el comportamiento del entrenamiento. 
    Requisitos: 3 llamadas distintas a la biblioteca 'statistics'. 
    """ 
    print("--- Análisis de Rendimiento ---")
    
    #validación con if/else
    if len(lista_loss) > 1 and len(latencias) > 0:
        #1. statistics.mean(): media de pérdida
        media_loss = statistics.mean(lista_loss)
        #2. statistics.stdev(): desviación estándar
        stdev_loss = statistics.stdev(lista_loss)
        #3. statistics.median(): mediana de latencia
        mediana_latencia = statistics.median(latencias)

        print(f"Media de Loss: {media_loss:.4f}")
        print(f"Desviación Estándar de Loss: {stdev_loss:.4f} (Estabilidad)")
        print(f"Mediana de Latencia: {mediana_latencia:.4f} segundos\n")
    else:
        print("Error: No hay suficientes datos para calcular estadísticas completas.\n")

def calcular_rmse(predicciones, reales): 
    """ 
    Usa la biblioteca 'math' para calcular el Root Mean Squared Error (RMSE). 
    Requisitos: 3 llamadas distintas a la biblioteca 'math'. 
    """ 
    #validación con if/else para evitar fallos
    if len(predicciones) == 0 or len(predicciones) != len(reales):
        print("Datos inválidos para calcular RMSE.")
        return 0.0

    suma_errores_cuadrados = 0
    for i in range(len(predicciones)):
        diferencia = predicciones[i] - reales[i]
        #1. math.pow(): aplicar función de potencia para elevar diferencias al cuadrado [cite: 35, 36]
        error_cuadrado = math.pow(diferencia, 2)
        suma_errores_cuadrados += error_cuadrado

    mse = suma_errores_cuadrados / len(predicciones)
    #2. math.sqrt(): calcular la raíz cuadrada para la métrica RMSE 
    rmse = math.sqrt(mse)
    #3. math.ceil(): usar redondeo hacia arriba para el cálculo final de epochs 
    epochs_extra = math.ceil(rmse * 5)

    print("--- Métricas de Error ---")
    print(f"RMSE Calculado: {rmse:.4f}")
    print(f"Recomendación: Entrenar por {epochs_extra} epochs adicionales.\n")
    
    return rmse

# ========================================== 
# 4. PROGRAMA PRINCIPAL (PUNTO DE ENTRADA) 
# ========================================== 
if __name__ == "__main__": 
    print("=== INICIANDO SIMULADOR DE AGENTES DE IA ===") 

    #1. obtenemos información del sistema
    obtener_info_sistema()
    
    #2. simulamos los datos (pasando nuestra constante MAX_EPOCHS)
    loss_simulado, latencias_simuladas = simular_metricas_entrenamiento(MAX_EPOCHS)
    
    #3. analizamos el rendimiento con statistics
    analizar_rendimiento(loss_simulado, latencias_simuladas)

    #para el cálculo del RMSE, comparamos nuestras "predicciones" (loss simulado)
    #contra un escenario "real" ideal donde el loss esperado era 0.0
    valores_reales_ideales = [0.0] * len(loss_simulado)
    
    #4. calculamos el error final
    rmse_final = calcular_rmse(loss_simulado, valores_reales_ideales)

    #5. validación final y salida del sistema
    if rmse_final > UMBRAL_ERROR_CRITICO:
        print(f"¡ALERTA CRÍTICA! El RMSE ({rmse_final:.4f}) superó el umbral de {UMBRAL_ERROR_CRITICO}.")
        print("Abortando proceso por inestabilidad de la red neuronal...")
        #sys.exit(): Forzar salida limpia del programa si es crítico (3er llamado a sys) 
        sys.exit(1)
    else:
        print("Simulación finalizada exitosamente. El agente es estable.")

"""
CUESTIONARIO DE ANÁLISIS DE BIBLIOTECAS (10 PUNTOS)
Deberás responder las siguientes 5 preguntas teóricas al final de tu código, utilizándolo como comentarios multilínea ("):

1. Uso de Objetos y Métodos: En tu código, al usar datetime.datetime.now(), ¿cuál es el objeto/clase y cuál es el método que estás llamando? Explica cómo se relaciona esto con el concepto de biblioteca externa.
R= el primer datetime es la libreria, el segundo es la clase y 
now() el metodo. usar esto nos ahorra programar cosas desde cero 
porque alguien mas ya lo hizo y nomas lo instanciamos.

2. Diferenciación Técnica: ¿Qué diferencia existe en la sintaxis de tu código al importar un módulo completo (ej: import math) versus importar un método específico (ej: from math import sqrt) al momento de invocar sus funciones?
R= con import math traes todo pero siempre debes poner math.sqrt(). 
si usas from math import sqrt lo llamas directo nomas poniendo sqrt() 
y es mas practico.

3. Flujo y Lógica: Describe brevemente la secuencia lógica de pasos que implementaste para conectar los datos generados por tu función de simulación con la función que calcula el error (RMSE).
R= la funcion de simular guarda los loss random en una lista. 
luego en el main le mando esa lista a la funcion de rmse junto 
a una lista de puros ceros reales para poder restarlos y hacer el calculo.

4. Mapeo de Tipos de Datos: Identifica al menos dos tipos de datos complejos (colecciones) que utilizaste para organizar los resultados de tus análisis y justifica por qué elegiste esa estructura en lugar de variables simples.
R= use listas para el loss y latencias porque es mas facil ir metiendo 
datos con append en cada iteracion. hacer variables separadas (loss1, loss2) 
seria inviable y statistics a fuerza necesita listas.

5. Autoevaluación de Abstracción: Al utilizar las funciones de la biblioteca statistics, ¿tuviste que programar la fórmula matemática matemática de la desviación estándar? Relaciona esto con el concepto de Abstracción visto en clase.
R= no, no programe la formula. de eso trata la abstraccion, la 
libreria hace toda la matematica compleja por debajo y yo solo pido 
el resultado sin preocuparme de como lo hace.
"""