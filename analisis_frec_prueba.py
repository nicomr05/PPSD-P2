from collections import Counter
import string

def decrypt_substitution_cipher(text, substitution_map):
    decrypted_text = "".join(substitution_map.get(char, char) for char in text)
    return decrypted_text

def analyze_frequencies(text):
    frequencies = Counter(text)
    total_chars = sum(frequencies.values())
    sorted_freq = sorted(frequencies.items(), key=lambda x: x[1], reverse=True)
    return sorted_freq

def main():
    encrypted_text = "TFSQWKXDQRTSQQXKGKQEXQFRGTSZOTDHGHQ..."
    
    # Análisis de frecuencia del texto encriptado
    frequencies = analyze_frequencies(encrypted_text)
    print("Frecuencia de caracteres en el texto encriptado:")
    for char, freq in frequencies:
        print(f"{char}: {freq}")
    
    # Mapeo inicial (debe ajustarse según el análisis manual)
    substitution_map = {
        'T': 'E', 'F': 'T', 'S': 'A', 'Q': 'O', 'W': 'I', 'K': 'N', 'X': 'S',
        'D': 'H', 'R': 'R', 'G': 'D', 'O': 'L', 'L': 'C', 'Z': 'U', 'H': 'M',
        'P': 'Y', 'M': 'P', 'C': 'B', 'N': 'V', 'U': 'G', 'J': 'W', 'Y': 'F'
        # Agregar más letras según el análisis
    }
    
    decrypted_text = decrypt_substitution_cipher(encrypted_text, substitution_map)
    print("Texto descifrado:")
    print(decrypted_text)

if __name__ == "__main__":
    main()
