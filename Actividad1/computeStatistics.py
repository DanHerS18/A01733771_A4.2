import sys
import time
import math
from collections import Counter

def read_file(filename):
    """Lee el archivo y devuelve una lista de números."""
    try:
        with open(filename, 'r') as file:
            data = file.read().splitlines()
            numbers = []
            for line in data:
                try:
                    # Convertimos cada número en flotante
                    numbers.append(float(line))
                except ValueError:
                    # Si el valor no se puede convertir, mostrar un error 
                    print(f"Advertencia: '{line}' no es un número válido.")
            return numbers
    except FileNotFoundError:
        print(f"Error: El archivo '{filename}' no se encuentra.")
        sys.exit(1)

def calculate_mean(numbers):
    """Calcula la media de una lista de números."""
    return sum(numbers) / len(numbers)

def calculate_median(numbers):
    """Calcula la mediana de una lista de números."""
    numbers.sort()
    n = len(numbers)
    if n % 2 == 1:
        return numbers[n // 2]
    else:
        mid1 = numbers[n // 2 - 1]
        mid2 = numbers[n // 2]
        return (mid1 + mid2) / 2

def calculate_mode(numbers):
    """Calcula la moda de una lista de números."""
    count = Counter(numbers)
    max_count = max(count.values())
    mode = [k for k, v in count.items() if v == max_count]
    return mode

def calculate_variance(numbers, mean):
    """Calcula la varianza de una lista de números."""
    return sum((x - mean) ** 2 for x in numbers) / len(numbers)

def calculate_standard_deviation(variance):
    """Calcula la desviación estándar dada la varianza."""
    return math.sqrt(variance)

def main():
    if len(sys.argv) != 2:
        print("Uso: python computeStatistics.py <archivo_con_datos>")
        sys.exit(1)
    
    filename = sys.argv[1]
    
    # Empieza el temporizador
    start_time = time.time()
    
    # Lee el archivo y obtiene los números
    numbers = read_file(filename)
    
    if not numbers:
        print("No se encontraron números válidos en el archivo.")
        sys.exit(1)
    
    # Calcular estadísticas
    mean = calculate_mean(numbers)
    median = calculate_median(numbers)
    mode = calculate_mode(numbers)
    variance = calculate_variance(numbers, mean)
    standard_deviation = calculate_standard_deviation(variance)
    
    # Mostrar los resultados en consola
    print(f"Media: {mean}")
    print(f"Mediana: {median}")
    print(f"Moda: {mode}")
    print(f"Varianza: {variance}")
    print(f"Desviación estándar: {standard_deviation}")
    
    # Calculamos el tiempo de ejecución
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Tiempo de ejecución: {execution_time:.4f} segundos")
    
    # Guardamos los resultados en un archivo
    with open('StatisticsResults.txt', 'w') as result_file:
        result_file.write(f"Media: {mean}\n")
        result_file.write(f"Mediana: {median}\n")
        result_file.write(f"Moda: {mode}\n")
        result_file.write(f"Varianza: {variance}\n")
        result_file.write(f"Desviación estándar: {standard_deviation}\n")
        result_file.write(f"Tiempo de ejecución: {execution_time:.4f} segundos\n")

if __name__ == "__main__":
    main()
