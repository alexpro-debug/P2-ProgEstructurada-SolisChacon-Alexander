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

# TODO: Implementar lógica 
pass 
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

# TODO: Implementar lógica 
pass 
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

# TODO: Implementar lógica 
pass 
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

# TODO: Implementar lógica 
pass 
# ========================================== 
# 4. PROGRAMA PRINCIPAL (PUNTO DE ENTRADA) 
# ========================================== 
if __name__ == "__main__": 
    print("=== INICIANDO SIMULADOR DE AGENTES DE IA ===") 
# TODO: Invocar las funciones, orquestar el flujo y mostrar reportes ordenados. 