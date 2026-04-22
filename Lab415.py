# Lista de provincias y comarcas de Panamá (Inmutable)
provincias_panama = (
    "Bocas del Toro", "Coclé", "Colón", "Chiriquí", "Darién", 
    "Herrera", "Los Santos", "Panamá", "Veraguas", "Panamá Oeste",
    "Guna Yala", "Emberá-Wounaan", "Ngäbe-Buglé", "Madugandí", "Wargandí"
)

print("Listado oficial de provincias y comarcas (Orden Protegido):")
for i, lugar in enumerate(provincias_panama, 1):
    print(f"{i}. {lugar}")

# Intento de cambio (esto lanzará un error si se descomenta)
# provincias_panama[0] = "Nueva Provincia"