"""
EJEMPLOS DE GRAFOS EN PYTHON
Implementación de varios tipos de grafos y algoritmos
"""

from collections import deque, defaultdict
import json


class Grafo:
    """Implementación de un Grafo No Dirigido"""
    
    def __init__(self, dirigido=False):
        """Inicializa el grafo"""
        self.grafo = defaultdict(list)
        self.dirigido = dirigido
    
    def agregar_arista(self, u, v, peso=1):
        """Agrega una arista al grafo"""
        self.grafo[u].append((v, peso))
        if not self.dirigido:
            self.grafo[v].append((u, peso))
    
    def bfs(self, inicio):
        """Búsqueda en Amplitud (BFS)"""
        visitados = set()
        cola = deque([inicio])
        resultado = []
        visitados.add(inicio)
        
        while cola:
            vertice = cola.popleft()
            resultado.append(vertice)
            
            for vecino, _ in self.grafo[vertice]:
                if vecino not in visitados:
                    visitados.add(vecino)
                    cola.append(vecino)
        
        return resultado
    
    def dfs(self, inicio):
        """Búsqueda en Profundidad (DFS)"""
        visitados = set()
        resultado = []
        
        def _dfs(vertice):
            visitados.add(vertice)
            resultado.append(vertice)
            
            for vecino, _ in self.grafo[vertice]:
                if vecino not in visitados:
                    _dfs(vecino)
        
        _dfs(inicio)
        return resultado
    
    def dijkstra(self, inicio):
        """Algoritmo de Dijkstra para camino más corto"""
        distancias = {vertice: float('inf') for vertice in self.grafo}
        distancias[inicio] = 0
        visitados = set()
        
        while len(visitados) < len(self.grafo):
            no_visitados = {v: distancias[v] for v in self.grafo if v not in visitados}
            
            if not no_visitados:
                break
            
            vertice_actual = min(no_visitados, key=no_visitados.get)
            visitados.add(vertice_actual)
            
            for vecino, peso in self.grafo[vertice_actual]:
                nueva_distancia = distancias[vertice_actual] + peso
                if nueva_distancia < distancias[vecino]:
                    distancias[vecino] = nueva_distancia
        
        return distancias
    
    def mostrar(self):
        """Muestra la lista de adyacencia del grafo"""
        print("\n--- Lista de Adyacencia ---")
        for vertice in sorted(self.grafo.keys()):
            vecinos = ', '.join([f"{v}({p})" for v, p in self.grafo[vertice]])
            print(f"{vertice}: [{vecinos}]")


def ejemplo_grafo_basico():
    """Ejemplo 1: Grafo básico no dirigido"""
    print("\n" + "="*60)
    print("EJEMPLO 1: Grafo No Dirigido Básico")
    print("="*60)
    
    g = Grafo(dirigido=False)
    
    # Agregar aristas
    aristas = [('A', 'B'), ('A', 'C'), ('B', 'D'), ('C', 'D'), ('D', 'E')]
    
    print("\n--- Agregando aristas ---")
    for u, v in aristas:
        g.agregar_arista(u, v)
        print(f"Arista agregada: {u} - {v}")
    
    g.mostrar()
    
    # BFS
    print("\n--- BFS desde A ---")
    bfs_resultado = g.bfs('A')
    print(f"Orden de recorrido: {bfs_resultado}")
    
    # DFS
    print("\n--- DFS desde A ---")
    dfs_resultado = g.dfs('A')
    print(f"Orden de recorrido: {dfs_resultado}")


def ejemplo_grafo_ponderado():
    """Ejemplo 2: Grafo ponderado (camino más corto)"""
    print("\n" + "="*60)
    print("EJEMPLO 2: Grafo Ponderado - Dijkstra")
    print("="*60)
    
    g = Grafo(dirigido=False)
    
    # Agregar aristas con pesos
    aristas_ponderadas = [
        ('A', 'B', 4),
        ('A', 'C', 2),
        ('B', 'C', 1),
        ('B', 'D', 5),
        ('C', 'D', 8),
        ('C', 'E', 10),
        ('D', 'E', 2)
    ]
    
    print("\n--- Grafo ponderado (distancias) ---")
    for u, v, peso in aristas_ponderadas:
        g.agregar_arista(u, v, peso)
        print(f"Arista: {u} - {v} (peso: {peso})")
    
    # Dijkstra
    print("\n--- Dijkstra desde A ---")
    distancias = g.dijkstra('A')
    print("Distancia más corta desde A:")
    for vertice, distancia in sorted(distancias.items()):
        print(f"  A → {vertice}: {distancia}")


def ejemplo_grafo_dirigido():
    """Ejemplo 3: Grafo dirigido"""
    print("\n" + "="*60)
    print("EJEMPLO 3: Grafo Dirigido")
    print("="*60)
    
    g = Grafo(dirigido=True)
    
    # Agregar aristas dirigidas
    aristas_dirigidas = [
        ('A', 'B'),
        ('A', 'C'),
        ('B', 'D'),
        ('C', 'B'),
        ('D', 'C'),
        ('D', 'E')
    ]
    
    print("\n--- Aristas dirigidas (A → B) ---")
    for u, v in aristas_dirigidas:
        g.agregar_arista(u, v)
        print(f"Arista: {u} → {v}")
    
    g.mostrar()
    
    print("\n--- BFS desde A ---")
    bfs_resultado = g.bfs('A')
    print(f"Recorrido: {bfs_resultado}")


def ejemplo_red_social():
    """Ejemplo 4: Aplicación real - Red Social"""
    print("\n" + "="*60)
    print("EJEMPLO 4: Red Social (Amistades)")
    print("="*60)
    
    amistades = Grafo(dirigido=False)
    
    # Crear red de amigos
    personas = [
        ('Carlos', 'María'),
        ('Carlos', 'Juan'),
        ('María', 'Ana'),
        ('Juan', 'Ana'),
        ('Juan', 'Pedro'),
        ('Ana', 'Pedro')
    ]
    
    print("\n--- Agregando amistades ---")
    for persona1, persona2 in personas:
        amistades.agregar_arista(persona1, persona2)
        print(f"{persona1} es amigo de {persona2}")
    
    print("\n--- Amigos de Carlos (BFS) ---")
    amigos = amistades.bfs('Carlos')
    print(f"Red de {amigos[0]}: {amigos[1:]}")
    
    print("\n--- Todos en la red (DFS) ---")
    red = amistades.dfs('Carlos')
    print(f"Personas en la red: {red}")


def ejemplo_mapa_ciudades():
    """Ejemplo 5: Aplicación real - Rutas entre ciudades"""
    print("\n" + "="*60)
    print("EJEMPLO 5: Mapa de Ciudades (Dijkstra)")
    print("="*60)
    
    mapa = Grafo(dirigido=False)
    
    # Distancias entre ciudades
    rutas = [
        ('Madrid', 'Barcelona', 600),
        ('Madrid', 'Valencia', 360),
        ('Barcelona', 'Valencia', 400),
        ('Madrid', 'Sevilla', 540),
        ('Valencia', 'Sevilla', 540)
    ]
    
    print("\n--- Red de carreteras (distancias en km) ---")
    for ciudad1, ciudad2, distancia in rutas:
        mapa.agregar_arista(ciudad1, ciudad2, distancia)
        print(f"{ciudad1} ↔ {ciudad2}: {distancia} km")
    
    print("\n--- Ruta más corta desde Madrid ---")
    distancias = mapa.dijkstra('Madrid')
    for ciudad, distancia in sorted(distancias.items()):
        if ciudad != 'Madrid':
            print(f"Madrid → {ciudad}: {distancia} km")


def main():
    """Función principal - Ejecuta todos los ejemplos"""
    print("\n" + "="*60)
    print("EJEMPLOS DE GRAFOS EN PYTHON")
    print("="*60)
    
    ejemplo_grafo_basico()
    ejemplo_grafo_ponderado()
    ejemplo_grafo_dirigido()
    ejemplo_red_social()
    ejemplo_mapa_ciudades()
    
    print("\n" + "="*60)
    print("FIN DE LOS EJEMPLOS")
    print("="*60 + "\n")


if __name__ == "__main__":
    main()
