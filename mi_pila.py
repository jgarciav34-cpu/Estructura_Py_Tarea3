from pasajero import Pasajero


class MiPila:
    """Pila (LIFO) hecha a mano sobre un arreglo de tamaño fijo.
    datos -> [fondo, ..., TOPE, None, None]
    TOPE  -> datos[cantidad - 1]  (el último que entró: el único que se ve y el único que sale)
    ⛔ Mismas prohibiciones que MiLista: sin append, pop, insert, remove, index,
       sort, reverse, copy, len(), in, slicing ni comprensiones.
    """

    def __init__(self, capacidad=10):
        self.datos = [None] * capacidad
        self.capacidad = capacidad
        self.cantidad = 0

    def apilar(self, pasajero):                      # ✅ resuelto (= añadir de MiLista)
        if self.cantidad == self.capacidad:
            print("  ⚠ La pila está llena")
            return False
        self.datos[self.cantidad] = pasajero          # el nuevo queda encima: es el TOPE
        self.cantidad = self.cantidad + 1
        return True

    def listar(self):                                 # ✅ EJEMPLO: del TOPE al FONDO
        if self.cantidad == 0:
            print("  (pila vacía)")
            return
        for i in range(self.cantidad - 1, -1, -1):    # cantidad-1, ..., 1, 0  (hacia atrás)
            if i == self.cantidad - 1:
                print(f"  [{i}] {self.datos[i]}  ← TOPE")
            elif i == 0:
                print(f"  [{i}] {self.datos[i]}  ← FONDO")
            else:
                print(f"  [{i}] {self.datos[i]}")

    # ------- ✍ IMPLEMENTA (tabla 3) · recorre SIEMPRE del tope al fondo -------
    def desapilar(self):
        if self.cantidad == 0:
            print("   (pila vacia)")
            return None
        aux = self.datos[self.cantidad-1]
        self.datos[self.cantidad-1] = None
        self.cantidad -= 1
        return aux

    def ver_tope(self):
        if self.cantidad == 0:
            print("   (pila vacia)")
            return None
        return self.datos[self.cantidad-1]

    def buscar(self, numero):
        for i in range(self.cantidad - 1, -1, -1):    # cantidad-1, ..., 1, 0  (hacia atrás)
            if numero == self.datos[i].numero:
                return i
        return -1

    def modificar(self, numero, nuevo_destino, nuevo_asiento):
        pos = self.buscar(numero)
        if pos == -1:
            return False
        self.datos[pos].numero = numero
        self.datos[pos].destino = nuevo_destino
        self.datos[pos].asiento = nuevo_asiento
        return True
        

    def eliminar_por_numero(self, numero):
        pila_aux = MiPila(self.capacidad)
        eliminado = False

        # 1. Desapilamos de la original a la auxiliar hasta encontrarlo
        while self.cantidad > 0:
            pasajero = self.desapilar()
            if pasajero.numero == numero:
                eliminado = True
                break # Lo descartamos (no lo apilamos en aux) y paramos de buscar
            else:
                pila_aux.apilar(pasajero)

        # 2. Devolvemos los pasajeros de la auxiliar a la pila original
        while pila_aux.cantidad > 0:
            self.apilar(pila_aux.desapilar())
            
        return eliminado

    def copiar(self):
        nueva = MiPila(self.capacidad)
        for i in range(self.cantidad):
            nueva.apilar(self.datos[i])
        return nueva

    def longitud(self):
        return self.cantidad

    def esta_vacia(self):
        return self.cantidad==0
    