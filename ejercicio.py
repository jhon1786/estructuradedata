"""
ESTRUCTURA DE DATOS: COLA (Queue)
Una Cola es una estructura de datos que sigue el principio FIFO (First In, First Out)
El primer elemento en entrar es el primero en salir.
"""

class Cola:
    """Implementación de una Cola (Queue) usando una lista"""
    
    def __init__(self):
        """Inicializa una cola vacía"""
        self.elementos = []
    
    def encolar(self, elemento):
        """Agrega un elemento al final de la cola (enqueue)"""
        self.elementos.append(elemento)
        print(f"✓ {elemento} encolado. Cola: {self.elementos}")
    
    def desencolar(self):
        """Elimina y retorna el primer elemento de la cola (dequeue)"""
        if self.esta_vacia():
            print("✗ Error: La cola está vacía. No se puede desencolar.")
            return None
        elemento = self.elementos.pop(0)
        print(f"✓ {elemento} desencolado. Cola: {self.elementos}")
        return elemento
    
    def primero(self):
        """Retorna el primer elemento sin eliminarlo (peek)"""
        if self.esta_vacia():
            print("✗ La cola está vacía")
            return None
        return self.elementos[0]
    
    def esta_vacia(self):
        """Verifica si la cola está vacía"""
        return len(self.elementos) == 0
    
    def tamano(self):
        """Retorna la cantidad de elementos en la cola"""
        return len(self.elementos)
    
    def mostrar(self):
        """Muestra todos los elementos de la cola"""
        if self.esta_vacia():
            print("Cola vacía: []")
        else:
            print(f"Cola: {self.elementos}")


def ejemplo_basico():
    """Ejemplo básico de operaciones en una cola"""
    print("\n" + "="*60)
    print("EJEMPLO 1: Operaciones Básicas de una Cola")
    print("="*60)
    
    cola = Cola()
    
    # Encolar elementos
    print("\n--- Encolando elementos ---")
    cola.encolar("Persona 1")
    cola.encolar("Persona 2")
    cola.encolar("Persona 3")
    cola.encolar("Persona 4")
    
    # Ver el primero
    print(f"\nPrimer elemento (sin remover): {cola.primero()}")
    print(f"Tamaño de la cola: {cola.tamano()}")
    
    # Desencolar elementos
    print("\n--- Desencolando elementos ---")
    cola.desencolar()
    cola.desencolar()
    
    # Mostrar estado actual
    cola.mostrar()


def ejemplo_simulacion_banco():
    """Simula un sistema de atención en un banco"""
    print("\n" + "="*60)
    print("EJEMPLO 2: Simulación de Fila en un Banco")
    print("="*60)
    
    cola_banco = Cola()
    
    print("\n--- Clientes llegando al banco ---")
    clientes = ["Carlos", "María", "Juan", "Ana", "Pedro"]
    for cliente in clientes:
        cola_banco.encolar(cliente)
    
    print(f"\nTotal de clientes esperando: {cola_banco.tamano()}")
    
    print("\n--- Atendiendo clientes ---")
    while not cola_banco.esta_vacia():
        cliente = cola_banco.desencolar()
        print(f"   Atendiendo a: {cliente}")
    
    print("\n✓ Todos los clientes fueron atendidos")


def ejemplo_simulacion_impresora():
    """Simula una cola de impresión"""
    print("\n" + "="*60)
    print("EJEMPLO 3: Simulación de Cola de Impresión")
    print("="*60)
    
    cola_impresion = Cola()
    
    print("\n--- Enviando documentos a imprimir ---")
    documentos = [
        "Reporte_Ventas.pdf",
        "Presentación.pptx",
        "Contrato.docx",
        "Factura.pdf",
        "Carta.docx"
    ]
    
    for doc in documentos:
        cola_impresion.encolar(doc)
    
    print(f"\nDocumentos en la cola: {cola_impresion.tamano()}")
    
    print("\n--- Imprimiendo documentos (en orden FIFO) ---")
    contador = 1
    while not cola_impresion.esta_vacia():
        doc = cola_impresion.desencolar()
        print(f"   {contador}. Imprimiendo: {doc}")
        contador += 1


def ejemplo_comparacion():
    """Compara Cola vs Pila (muestra la diferencia FIFO vs LIFO)"""
    print("\n" + "="*60)
    print("EJEMPLO 4: Comparación COLA (FIFO) vs PILA (LIFO)")
    print("="*60)
    
    # COLA (FIFO)
    print("\n--- COLA (First In, First Out) ---")
    cola = Cola()
    numeros = [1, 2, 3, 4, 5]
    for num in numeros:
        cola.encolar(num)
    
    print("\nSacando elementos:")
    resultado_cola = []
    while not cola.esta_vacia():
        resultado_cola.append(cola.desencolar())
    print(f"Orden de salida: {resultado_cola}")
    
    # PILA (LIFO) - para comparar
    print("\n--- PILA (Last In, First Out) - Para comparación ---")
    pila = []
    for num in numeros:
        pila.append(num)
    
    print("\nSacando elementos:")
    resultado_pila = []
    while pila:
        resultado_pila.append(pila.pop())
    print(f"Orden de salida: {resultado_pila}")


def main():
    """Función principal"""
    print("\n" + "="*60)
    print("EJERCICIO DE ESTRUCTURA DE DATOS: COLA (QUEUE)")
    print("="*60)
    
    # Ejecutar todos los ejemplos
    ejemplo_basico()
    ejemplo_simulacion_banco()
    ejemplo_simulacion_impresora()
    ejemplo_comparacion()
    
    print("\n" + "="*60)
    print("FIN DEL EJERCICIO")
    print("="*60 + "\n")


if __name__ == "__main__":
    main()
