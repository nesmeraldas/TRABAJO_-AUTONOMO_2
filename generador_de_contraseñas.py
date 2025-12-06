#ANTES DE EMPEZAR CON LAS LINEAS DE CODIGO IMPORTAMOS LOS MODULOS QUE NOS PERMITEN GENERAR EL PROGRAMA
import random
import time


print("GENERADOR DE CONTRASEÑAS SEGURAS")

# Solicitar que tipo de contraseña deseas generar
print("Seleccione el tipo de contraseña:")
print("1. Simple (letras y números)")
print("2. Compleja (letras, números y símbolos)")

tipo = input("Opción (1 o 2): ")

# Solicitar la longitud
longitud = int(input("Ingrese la longitud de la contraseña: "))


# Validar que sea 1 o 2
if tipo not in ["1", "2"]:
    print("Opción no válida. Debe ingresar 1 o 2.")
    exit()

tipo = int(tipo)

# Definir caracteres según tipo
if tipo == 1:
    caracteres = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
else:
    caracteres = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%&*?"

# Generar la contraseña
password = ""
for _ in range(longitud):
    password += random.choice(caracteres)
time.sleep(5)
print("Contraseña segura generada:", password)
