# 1. Literal de bytes
mi_byte = b"\xFF"

# 2. Constructor bytes a partir de un entero
mi_byte_dos = bytes([255])

# Verificación
print(type(mi_byte))
print(mi_byte[0]) # Debería imprimir 255