# ANTES DE EMPEZAR CON LAS LINEAS DE CODIGO IMPORTAMOS LOS MODULOS QUE NOS PERMITEN GENERAR EL PROGRAMA
import random
import time

# === NUEVA ESTRUCTURA DE DATOS (DICCIONARIO) ===
CHARSETS = {
    "1": "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789",
    "2": "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%&*?"
}

# === NUEVA FUNCIÓN: pedir tipo de contraseña ===
def solicitar_tipo():
    print("Seleccione el tipo de contraseña:")
    print("1. Simple (letras y números)")
    print("2. Compleja (letras, números y símbolos)")
    tipo = input("Opción (1 o 2): ")

    # validación con bucle para no salir del programa
    while tipo not in CHARSETS:
        print("Opción no válida. Debe ingresar 1 o 2.")
        tipo = input("Opción (1 o 2): ")

    return tipo

# === NUEVA FUNCIÓN: pedir longitud de la contraseña ===
def solicitar_longitud():
    while True:
        try:
            longitud = int(input("Ingrese la longitud de la contraseña (mínimo 4): "))
            if longitud < 4:
                print("La longitud mínima recomendada es 4.")
            else:
                return longitud
        except ValueError:
            print("Debe ingresar un número entero.")

# === NUEVA FUNCIÓN: generar contraseña ===
def generar_contraseña(tipo, longitud):
    caracteres = CHARSETS[tipo]
    # uso de comprensión de listas / join para generar la contraseña
    return "".join(random.choice(caracteres) for _ in range(longitud))

# === NUEVA FUNCIÓN: evaluar la seguridad de la contraseña ===
def evaluar_seguridad(password):
    longitud = len(password)
    tiene_mayus = any(c.isupper() for c in password)
    tiene_minus = any(c.islower() for c in password)
    tiene_num = any(c.isdigit() for c in password)
    tiene_simbolo = any(not c.isalnum() for c in password)

    puntaje = 0
    if longitud >= 8:
        puntaje += 1
    if longitud >= 12:
        puntaje += 1
    if tiene_mayus and tiene_minus:
        puntaje += 1
    if tiene_num:
        puntaje += 1
    if tiene_simbolo:
        puntaje += 1

    if puntaje <= 2:
        nivel = "Débil"
    elif puntaje <= 4:
        nivel = "Media"
    else:
        nivel = "Fuerte"

    return nivel, puntaje

# === NUEVA FUNCIÓN: mostrar historial (usa lista como estructura de datos) ===
def mostrar_historial(historial):
    if not historial:
        print("Todavía no has generado ninguna contraseña.")
        return

    print("\nHistorial de contraseñas generadas:")
    for i, item in enumerate(historial, start=1):
        pw, tipo, longitud, nivel = item
        print(f"{i}. {pw} | Tipo: {tipo} | Longitud: {longitud} | Seguridad: {nivel}")

# === NUEVA FUNCIÓN PRINCIPAL: organiza todo el flujo del programa ===
def main():
    historial = []  # NUEVA ESTRUCTURA DE DATOS: lista para guardar contraseñas
    print("GENERADOR DE CONTRASEÑAS SEGURAS")

    while True:
        tipo = solicitar_tipo()
        longitud = solicitar_longitud()

        print("\nGenerando contraseña...")
        time.sleep(0.5)  # ahora sí se usa el módulo time

        password = generar_contraseña(tipo, longitud)
        nivel, puntaje = evaluar_seguridad(password)

        print("\nTu contraseña generada es:")
        print(password)
        print(f"Nivel de seguridad: {nivel} (puntaje: {puntaje}/5)")

        # guardamos datos en el historial (lista de tuplas)
        historial.append((
            password,
            "Simple" if tipo == "1" else "Compleja",
            longitud,
            nivel
        ))

        opcion = input("\n¿Deseas generar otra contraseña? (s/n, h = ver historial): ").lower()

        if opcion == "h":
            mostrar_historial(historial)
            opcion = input("\n¿Deseas generar otra contraseña? (s/n): ").lower()

        if opcion != "s":
            print("Gracias por usar el generador de contraseñas.")
            break

# Punto de entrada del programa
if __name__ == "__main__":
    main()