# Lab73.py
import string

def contar_palabras_unicas(texto):
    
    texto_limpio = texto.translate(str.maketrans('', '', string.punctuation))
    
    palabras = texto_limpio.lower().split()
    
    return len(set(palabras))

def palabra_mas_larga(texto):
    palabras = texto.split()
    if not palabras:
        return ""
   
    return max(palabras, key=len)

def frecuencia_caracteres(texto):
  
    texto_filtrado = [char.lower() for char in texto if char != " "]
    total_caracteres = len(texto_filtrado)
    
    frecuencias = {}
    for char in texto_filtrado:
        frecuencias[char] = frecuencias.get(char, 0) + 1
    
    print("\n--- Frecuencia de Caracteres ---")
    for char, cuenta in sorted(frecuencias.items()):
        porcentaje = (cuenta / total_caracteres) * 100
        print(f"Letra '{char}': {cuenta} veces ({porcentaje:.2f}%)")

def flujo_principal():
    print("--- Analizador de Texto ---")
    texto_usuario = input("Introduce una cadena de texto larga:\n")
    
    if not texto_usuario.strip():
        print("No has introducido ningún texto.")
        return

    
    unicas = contar_palabras_unicas(texto_usuario)
    
    
    larga = palabra_mas_larga(texto_usuario)
    
    
    print("\n" + "="*30)
    print("REPORTE DE MÉTRICAS")
    print("="*30)
    print(f"Cantidad de palabras diferentes: {unicas}")
    print(f"La palabra más larga es: '{larga}'")
    
    
    frecuencia_caracteres(texto_usuario)
    print("="*30)

if __name__ == "__main__":
    flujo_principal()