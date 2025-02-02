import sys
import time

def read_file(filename):
    """Lee el archivo y devuelve una lista de números válidos."""
    numbers = []
    try:
        with open(filename, "r") as file:
            for line in file:
                line = line.strip()
                if line.replace(".", "", 1).isdigit() or (line.startswith("-") and line[1:].replace(".", "", 1).isdigit()):
                    numbers.append(int(float(line)))  # Convertimos a entero
                else:
                    print(f"Advertencia: '{line}' no es un número válido.")
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo '{filename}'.")
        sys.exit(1)
    return numbers

def decimal_to_binary(n):
    """Convierte un número decimal a binario usando divisiones sucesivas."""
    if n == 0:
        return "0"
    is_negative = n < 0
    n = abs(n)
    binary = ""
    while n > 0:
        binary = str(n % 2) + binary
        n //= 2
    return "-" + binary if is_negative else binary

def decimal_to_hexadecimal(n):
    """Convierte un número decimal a hexadecimal usando divisiones sucesivas."""
    if n == 0:
        return "0"
    is_negative = n < 0
    n = abs(n)
    hex_chars = "0123456789ABCDEF"
    hexadecimal = ""
    while n > 0:
        hexadecimal = hex_chars[n % 16] + hexadecimal
        n //= 16
    return "-" + hexadecimal if is_negative else hexadecimal

def write_results(filename, results, execution_time):
    """Escribe los resultados en un archivo de salida."""
    with open(filename, "w") as file:
        for result in results:
            file.write(result + "\n")
        file.write(f"\nTiempo de ejecución: {execution_time:.4f} segundos")

def main():
    if len(sys.argv) != 2:
        print("Uso: python convertNumbers.py fileWithData.txt")
        sys.exit(1)

    filename = sys.argv[1]
    start_time = time.time()

    numbers = read_file(filename)
    results = []

    for num in numbers:
        binary = decimal_to_binary(num)
        hexadecimal = decimal_to_hexadecimal(num)
        result = f"Número: {num} | Binario: {binary} | Hexadecimal: {hexadecimal}"
        print(result)
        results.append(result)

    execution_time = time.time() - start_time
    results.append(f"\nTiempo de ejecución: {execution_time:.4f} segundos")

    write_results("ConvertionResults.txt", results, execution_time)

if __name__ == "__main__":
    main()
