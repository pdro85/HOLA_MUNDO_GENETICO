# Importar la biblioteca random para generar valores aleatorios
import random

# Definir la cadena objetivo que se desea obtener a través del algoritmo
objetivo = "Hola, Mundo"

# Función para generar una cadena aleatoria del mismo tamaño que la cadena objetivo
def generar_cadena_aleatoria(longitud):
    # Utiliza la función random.choice para seleccionar caracteres aleatorios del conjunto dado
    return ''.join(random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ, ') for _ in range(longitud))

"""
zip(objetivo, cadena): Esta función empareja los caracteres de la cadena objetivo y la cadena dada en pares. 
Por ejemplo, si la cadena objetivo es "Hola, Mundo" y la cadena dada es "Hola, Amigo", 
zip emparejará ('H', 'H'), ('o', 'o'), ('l', 'l'), ('a', 'a'), (',', ','), (' ', 'A'), ('M', 'm'), ('u', 'i'), ('n', 'g'), ('d', 'o'), ('o', None).

for esperado, real in zip(objetivo, cadena): Esto itera sobre cada par de caracteres emparejados. 
La variable esperado representa un carácter de la cadena objetivo, mientras que real representa el carácter correspondiente en la cadena dada.

if esperado == real: Esta condición comprueba si el carácter en la cadena dada es igual al carácter en la cadena objetivo en la misma posición.

sum(1 for esperado, real in zip(objetivo, cadena) if esperado == real): Esto suma 1 por cada vez que un carácter en la cadena 
dada coincide con el carácter en la cadena objetivo. 
Al final, la función de aptitud devuelve el recuento total de caracteres que coinciden entre las dos cadenas.

En resumen, la función de aptitud calcula cuántos caracteres coinciden entre la cadena dada y la cadena objetivo. 
Este valor de aptitud se utiliza para evaluar la calidad de una solución en relación con el objetivo del algoritmo genético.
"""
# Función de aptitud (fitness) que evalúa cuántos caracteres coinciden entre la cadena dada y la cadena objetivo
def aptitud(cadena):
    # Itera sobre cada par de caracteres en la cadena y cuenta cuántos coinciden con la cadena objetivo
    return sum(1 for esperado, real in zip(objetivo, cadena) if esperado == real)

# Función de reproducción que combina dos cadenas de texto (padre y madre) en un nuevo hijo
def reproduccion(padre, madre):
    # Selecciona un punto de cruce aleatorio para combinar las cadenas
    punto_corte = random.randint(0, len(padre) - 1)
    return padre[:punto_corte] + madre[punto_corte:]

# Parámetros del algoritmo
tamano_poblacion = 300  # Número de individuos en cada generación
probabilidad_mutacion = 0.1  # Probabilidad de que un gen mute
numero_generaciones = 3000  # Número máximo de generaciones

# Inicializar la población con cadenas de texto aleatorias del mismo tamaño que la cadena objetivo
poblacion = [generar_cadena_aleatoria(len(objetivo)) for _ in range(tamano_poblacion)]

# Algoritmo genético
for generacion in range(numero_generaciones):
    # Calcular la aptitud de cada individuo y ordenar la lista de acuerdo con la aptitud
    aptitudes = [(aptitud(cadena), cadena) for cadena in poblacion]
    # Ordena las aptitudes
    aptitudes.sort(reverse=True)
    # Verificar si se ha encontrado la cadena objetivo y detener el algoritmo si es así
    if aptitudes[0][1] == objetivo:
        break

    # Seleccionar el mejor individuo de la generación anterior
    nueva_poblacion = [aptitudes[0][1]]

    # Reproducción y mutación para generar el resto de la nueva población
    for _ in range(1, tamano_poblacion):
        # Seleccionar aleatoriamente dos individuos de la generación actual
        padre = random.choice(aptitudes)[1]
        madre = random.choice(aptitudes)[1]

        # Generar un nuevo individuo combinando los genes de los padres
        hijo = reproduccion(padre, madre)

        # Mutación: cambiar un carácter aleatorio con una cierta probabilidad
        if random.random() < probabilidad_mutacion:
            index_mutacion = random.randint(0, len(hijo) - 1)
            hijo = hijo[:index_mutacion] + random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ, ') + hijo[index_mutacion + 1:]

        # Agregar el nuevo individuo a la nueva población
        nueva_poblacion.append(hijo)

    # Reemplazar la población anterior con la nueva población
    poblacion = nueva_poblacion

# Imprimir la cadena objetivo y la generación en la que se encontró
mejor_cadena = aptitudes[0][1]
print(f"¡Encontrado en la generación {generacion}!: {mejor_cadena}")
