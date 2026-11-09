import os

# =====================================================================
#  DICCIONARIOS Y CONSTANTES
# =====================================================================
COLORES = {
    "ROJO": "\033[91m",
    "VERDE": "\033[92m",
    "AZUL": "\033[94m",
    "AMARILLO": "\033[93m",
    "CYAN": "\033[96m",
    "BLANCO": "\033[97m",
    "RESET": "\033[0m",
}

RESPUESTAS_SI = ("si", "sí", "s", "yes", "y")

# =====================================================================
#  FUNCIONES DE PANTALLA Y FLUJO
# =====================================================================
def limpiar_pantalla():
    """Limpia la consola dependiendo del sistema operativo (Windows o Mac/Linux)."""
    os.system("clear" if os.name == "posix" else "cls")

def pausar():
    """Pausa la ejecución para que el usuario alcance a leer los mensajes antes de limpiar."""
    print()
    imprimir_color("Presiona ENTER para continuar...", "CYAN")
    input()

# =====================================================================
#  FUNCIONES DE ESTILO Y MENSAJES
# =====================================================================
def imprimir_color(texto, color):
    codigo = COLORES.get(color, COLORES["BLANCO"])
    print(f"{codigo}{texto}{COLORES['RESET']}")

def imprimir_titulo(texto):
    """Limpia la pantalla y dibuja un encabezado centrado."""
    limpiar_pantalla()
    imprimir_color("=" * 60, "AZUL")
    print(f"{COLORES['BLANCO']}{texto.center(60)}{COLORES['RESET']}")
    imprimir_color("=" * 60, "AZUL")
    print()

def imprimir_exito(mensaje):
    imprimir_color(f"  ✓ {mensaje}", "VERDE")

def imprimir_error(mensaje):
    imprimir_color(f"  ✗ {mensaje}", "ROJO")

def imprimir_info(mensaje):
    imprimir_color(f"  ℹ {mensaje}", "CYAN")

def imprimir_advertencia(mensaje):
    imprimir_color(f"  ⚠ {mensaje}", "AMARILLO")

# =====================================================================
#  FUNCIONES DE LECTURA Y VALIDACIÓN
# =====================================================================
def confirmar(pregunta):
    """Útil para preguntar antes de eliminar (ej. ¿Seguro que desea eliminar al pasajero?)"""
    respuesta = input(f"  {COLORES['AMARILLO']}? {pregunta} (si/no): {COLORES['RESET']}").strip().lower()
    return respuesta in RESPUESTAS_SI

def leer_entero(mensaje):
    """Pide un número entero y repite hasta que sea válido."""
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            imprimir_error("Formato inválido. Debe ser un número entero.")