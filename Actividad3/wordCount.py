import sys
import time

def count_words(filename):
    word_freq = {}
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            for line in file:
                words = line.strip().split()  # Separar por espacios
                for word in words:
                    cleaned_word = ''.join(char.lower() for char in word if char.isalnum())  # Eliminar signos de puntuación
                    if cleaned_word:
                        word_freq[cleaned_word] = word_freq.get(cleaned_word, 0) + 1
    except FileNotFoundError:
        print(f"Error: El archivo '{filename}' no existe.")
        return None
    except Exception as e:
        print(f"Error al leer el archivo: {e}")
        return None
    return word_freq

def save_results(word_freq, elapsed_time):
    if word_freq is None:
        return
    with open("WordCountResults.txt", 'w', encoding='utf-8') as file:
        for word, count in sorted(word_freq.items()):
            file.write(f"{word}: {count}\n")
        file.write(f"\nTiempo de ejecución: {elapsed_time:.4f} segundos\n")

def main():
    if len(sys.argv) != 2:
        print("Uso: python wordCount.py <archivo>")
        return
    filename = sys.argv[1]
    
    start_time = time.time()
    word_freq = count_words(filename)
    elapsed_time = time.time() - start_time
    
    if word_freq is not None:
        print("Resultados:")
        for word, count in sorted(word_freq.items()):
            print(f"{word}: {count}")
        print(f"\nTiempo de ejecución: {elapsed_time:.4f} segundos")
        save_results(word_freq, elapsed_time)

if __name__ == "__main__":
    main()
