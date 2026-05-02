# Lab72.py
def generar_matriz_identidad():
    try:
        n = int(input("Introduce el orden de la matriz (N debe ser par): "))
        
        if n % 2 != 0:
            print("Error: El número N debe ser un número PAR.")
            return

        print(f"\nMatriz Identidad de orden {n}:")
        
        for i in range(n):
            fila = []
            for j in range(n):
                if i == j:
                    fila.append(1)
                else:
                    fila.append(0)
            
            
            print("\t".join(map(str, fila)))
            
    except ValueError:
        print("Error: Entrada no válida. Introduce un número entero.")

if __name__ == "__main__":
    generar_matriz_identidad()