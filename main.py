from pasajero import Pasajero
from mi_pila import MiPila
from mi_cola import MiCola

# Importamos las herramientas de nuestro nuevo archivo utils.py
from utils import (leer_entero, imprimir_titulo, imprimir_exito, 
                   imprimir_error, imprimir_info, imprimir_advertencia, 
                   pausar, confirmar)

pila = MiPila(10)
cola = MiCola(10)


# ------------------------- Funciones de apoyo -------------------------
def leer_pasajero():
    numero = leer_entero("  N.º de pasajero: ")
    nombre = input("  Nombre: ").strip()
    cedula = input("  Cédula: ").strip()
    edad = leer_entero("  Edad: ")
    fecha = input("  Fecha de vuelo (AAAA-MM-DD): ").strip()
    destino = input("  Destino: ").strip()
    asiento = input("  Asiento: ").strip().upper()
    return Pasajero(numero, nombre, cedula, edad, fecha, destino, asiento)


def datos_prueba():
    """Los 5 pasajeros de prueba en ORDEN DE LLEGADA (Diana llega primero, Elena última)."""
    return [
        Pasajero(1005, "Diana", "0923456789", 22, "2026-11-15", "Quito",  "12A"),
        Pasajero(1002, "Ana",   "0912345678", 28, "2026-11-15", "Lima",   "03C"),
        Pasajero(1009, "Luis",  "0987654321", 35, "2026-11-20", "Bogotá", "18F"),
        Pasajero(1004, "Beto",  "0934567890", 16, "2026-11-20", "Quito",  "07B"),
        Pasajero(1001, "Elena", "0901234567", 41, "2026-11-22", "Lima",   "01A"),
    ]


def mostrar_opciones(titulo, entrar, salir, ver):
    imprimir_titulo(titulo)
    print(f" 1. {entrar:<12}  2. Listar          3. {salir}")
    print(f" 4. {ver:<12}  5. Buscar          6. Modificar")
    print(" 7. Eliminar por número         8. Copiar")
    print(" 9. Longitud / ¿vacía?")
    print(" C. Cargar datos de prueba      0. Volver")
    print()


# ---------------------- MENÚ 1 · PILA ----------------------
def menu_pila():
    while True:
        mostrar_opciones("MENÚ 1 · PILA (LIFO)", "Apilar", "Desapilar", "Ver tope")
        op = input("  Opción: ").strip().upper()
        print()

        if op == "1":
            pasajero = leer_pasajero()
            if pila.apilar(pasajero):
                imprimir_exito("Apilado: ahora es el tope.")
        
        elif op == "2":
            pila.listar()
        
        elif op == "3":
            quitado = pila.desapilar()
            if quitado:
                imprimir_exito(f"Desapilado: {quitado.nombre}") 
            else:
                imprimir_advertencia("No se puede desapilar, la pila está vacía.")
        
        elif op == "4":
            tope = pila.ver_tope()
            if tope:
                imprimir_info(f"Tope: {tope.nombre} ({tope.numero})")
            else:
                imprimir_advertencia("La pila está vacía, no hay tope que mostrar.")
        
        elif op == "5":
            numero = leer_entero("  Ingrese número de pasajero a buscar: ")
            pos = pila.buscar(numero)
            if pos == -1:
                imprimir_error("Pasajero no encontrado.")
            else:
                imprimir_exito(f"Encontrado en la posición #{pos}:")
                print(f"  {pila.datos[pos]}")
        
        elif op == "6":
            numero = leer_entero("  Ingrese número de pasajero a modificar: ")
            pos = pila.buscar(numero)
            if pos == -1:
                imprimir_error("Pasajero no encontrado.")
            else:
                imprimir_info("Pasajero actual:")
                print(f"  {pila.datos[pos]}")
                nuevo_destino = input("  Ingrese nuevo destino: ").strip()
                nuevo_asiento = input("  Ingrese nuevo asiento: ").strip().upper()
                pila.modificar(pos, nuevo_destino, nuevo_asiento)    
                imprimir_exito("Modificado exitosamente.")
        
        elif op == "7":
            num = leer_entero("  Ingrese número de pasajero a eliminar: ")
            if confirmar(f"¿Seguro que desea eliminar al pasajero #{num}?"):
                if pila.eliminar_por_numero(num):
                    imprimir_exito("Eliminado correctamente.")
                else: 
                    imprimir_error("Pasajero no encontrado en la pila.")
            else:
                imprimir_info("Operación cancelada.")
        
        elif op == "8":
            copia = pila.copiar()
            if copia:
                imprimir_exito("Pila copiada exitosamente.")
                print("  Listando la copia:")
                copia.listar()
        
        elif op == "9":
            if pila.esta_vacia():
                imprimir_advertencia("La pila está vacía (0 pasajeros).")
            else:
                imprimir_info(f"La pila tiene {pila.longitud()} pasajeros guardados.")      
        
        elif op == "C":
            for p in datos_prueba():
                pila.apilar(p)
            imprimir_exito("Datos de prueba apilados correctamente.")

        elif op == "0":
            break
        
        else:
            imprimir_error("Opción no válida.")
        
        pausar()


# ---------------------- MENÚ 2 · COLA ----------------------
def menu_cola():
    while True:
        mostrar_opciones("MENÚ 2 · COLA (FIFO)", "Encolar", "Desencolar", "Ver frente")
        op = input("  Opción: ").strip().upper()
        print()

        if op == "1":
            pasajero = leer_pasajero()
            if cola.encolar(pasajero):
                imprimir_exito("Encolado: está al final de la fila.")
        
        elif op == "2":
            cola.listar()
        
        elif op == "3":
            quitado = cola.desencolar()
            if quitado:
                imprimir_exito(f"Desencolado: {quitado.nombre}") 
            else:
                imprimir_advertencia("No se puede desencolar, la cola está vacía.")
        
        elif op == "4":
            frente = cola.ver_frente()
            if frente:
                imprimir_info(f"Frente: {frente.nombre} ({frente.numero})")
            else:
                imprimir_advertencia("La cola está vacía, no hay frente que mostrar.")
        
        elif op == "5":
            numero = leer_entero("  Ingrese número de pasajero a buscar: ")
            pos = cola.buscar(numero)
            if pos == -1:
                imprimir_error("Pasajero no encontrado.")
            else:
                imprimir_exito(f"Encontrado en la posición #{pos}:")
                print(f"  {cola.datos[pos]}")
        
        elif op == "6":
            numero = leer_entero("  Ingrese número de pasajero a modificar: ")
            pos = cola.buscar(numero)
            if pos == -1:
                imprimir_error("Pasajero no encontrado.")
            else:
                imprimir_info("Pasajero actual:")
                print(f"  {cola.datos[pos]}")
                nuevo_destino = input("  Ingrese nuevo destino: ").strip()
                nuevo_asiento = input("  Ingrese nuevo asiento: ").strip().upper()
                cola.modificar(pos, nuevo_destino, nuevo_asiento)    
                imprimir_exito("Modificado exitosamente.")
        
        elif op == "7":
            num = leer_entero("  Ingrese número de pasajero a eliminar: ")
            if confirmar(f"¿Seguro que desea eliminar al pasajero #{num}?"):
                if cola.eliminar_por_numero(num):
                    imprimir_exito("Eliminado correctamente.")
                else: 
                    imprimir_error("Pasajero no encontrado en la cola.")
            else:
                imprimir_info("Operación cancelada.")
        
        elif op == "8":
            copia = cola.copiar()
            if copia:
                imprimir_exito("Cola copiada exitosamente.")
                print("  Listando la copia:")
                copia.listar()
        
        elif op == "9":
            if cola.esta_vacia():
                imprimir_advertencia("La cola está vacía (0 pasajeros).")
            else:
                imprimir_info(f"La cola tiene {cola.longitud()} pasajeros guardados.")      
        
        elif op == "C":
            for p in datos_prueba():
                cola.encolar(p)
            imprimir_exito("Datos de prueba encolados correctamente.")

        elif op == "0":
            break
        
        else:
            imprimir_error("Opción no válida.")
        
        pausar()


# ---------------------- MENÚ PRINCIPAL ----------------------
def main():
    while True:
        imprimir_titulo("TAREA PILAS Y COLAS · PASAJEROS ✈")
        print("  1. Menú 1 · Pila")
        print("  2. Menú 2 · Cola")
        print("  3. Salir\n")
        
        op = input("  Opción: ").strip()
        if op == "1":
            menu_pila()
        elif op == "2":
            menu_cola()
        elif op == "3":
            imprimir_info("¡Hasta pronto!")
            break
        else:
            imprimir_error("Opción no válida.")
            pausar()


if __name__ == "__main__":
    main()