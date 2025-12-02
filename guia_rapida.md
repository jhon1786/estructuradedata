# Guía Rápida de Grafos

## 1. Conceptos Clave

### ¿Qué es un Grafo?
- **Definición**: G = (V, E) donde V es un conjunto de vértices y E es un conjunto de aristas
- **Vértice**: Nodo o punto en el grafo
- **Arista**: Conexión entre dos vértices

### Características
- **Orden**: Número de vértices (|V|)
- **Tamaño**: Número de aristas (|E|)
- **Grado**: Número de aristas conectadas a un vértice

## 2. Tipos de Grafos

| Tipo | Características | Ejemplo |
|------|-----------------|---------|
| **No Dirigido** | Aristas sin dirección | Red de amistad |
| **Dirigido** | Aristas con dirección | Seguidores en Twitter |
| **Ponderado** | Aristas con pesos | Mapa de distancias |
| **Acíclico** | Sin ciclos | Árbol genealógico |
| **Completo** | Todos conectados con todos | Torneo round-robin |
| **Bipartito** | Vértices en dos grupos | Emparejamiento |

## 3. Representación

### Matriz de Adyacencia
```
Ventajas:
  ✓ O(1) para verificar arista
  ✓ Simple de implementar
  ✓ Buena para grafos densos

Desventajas:
  ✗ O(V²) memoria
  ✗ Ineficiente para grafos dispersos
```

### Lista de Adyacencia
```
Ventajas:
  ✓ O(V+E) memoria
  ✓ Eficiente para grafos dispersos
  ✓ Iteración rápida sobre vecinos

Desventajas:
  ✗ O(grado) para verificar arista
  ✗ Más compleja de implementar
```

## 4. Algoritmos de Búsqueda

### BFS (Búsqueda en Amplitud)
```python
def bfs(grafo, inicio):
    visitados = set()
    cola = deque([inicio])
    
    while cola:
        v = cola.popleft()
        if v not in visitados:
            visitados.add(v)
            cola.extend([u for u in grafo[v] if u not in visitados])
    
    return visitados
```

**Complejidad**: O(V + E)
**Uso**: Camino más corto en grafos no ponderados

### DFS (Búsqueda en Profundidad)
```python
def dfs(grafo, v, visitados=None):
    if visitados is None:
        visitados = set()
    
    visitados.add(v)
    
    for u in grafo[v]:
        if u not in visitados:
            dfs(grafo, u, visitados)
    
    return visitados
```

**Complejidad**: O(V + E)
**Uso**: Detectar ciclos, topología

## 5. Algoritmos de Camino Más Corto

### Dijkstra
```python
def dijkstra(grafo, inicio):
    distancias = {v: float('inf') for v in grafo}
    distancias[inicio] = 0
    visitados = set()
    
    while len(visitados) < len(grafo):
        u = min((v for v in grafo if v not in visitados), 
                key=lambda v: distancias[v])
        visitados.add(u)
        
        for v, peso in grafo[u]:
            if distancias[u] + peso < distancias[v]:
                distancias[v] = distancias[u] + peso
    
    return distancias
```

**Complejidad**: O(V²) o O((V+E)logV) con heap
**Limitación**: No funciona con pesos negativos

### Floyd-Warshall
```python
def floyd_warshall(grafo, n):
    dist = [[float('inf')] * n for _ in range(n)]
    
    for i in range(n):
        dist[i][i] = 0
    
    for u, v, w in grafo:
        dist[u][v] = w
    
    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    
    return dist
```

**Complejidad**: O(V³)
**Ventaja**: Calcula todas las distancias de una vez

## 6. Detección de Ciclos

### En Grafo No Dirigido
```python
def tiene_ciclo(grafo, n):
    visitados = [False] * n
    
    def dfs(v, padre):
        visitados[v] = True
        for u in grafo[v]:
            if not visitados[u]:
                if dfs(u, v):
                    return True
            elif u != padre:
                return True
        return False
    
    for i in range(n):
        if not visitados[i]:
            if dfs(i, -1):
                return True
    return False
```

### En Grafo Dirigido
```python
def tiene_ciclo_dirigido(grafo, n):
    color = [0] * n  # 0: blanco, 1: gris, 2: negro
    
    def dfs(v):
        color[v] = 1
        for u in grafo[v]:
            if color[u] == 1:
                return True
            if color[u] == 0 and dfs(u):
                return True
        color[v] = 2
        return False
    
    for i in range(n):
        if color[i] == 0:
            if dfs(i):
                return True
    return False
```

## 7. Componentes Conectadas

```python
def componentes_conectadas(grafo, n):
    visitados = [False] * n
    componentes = []
    
    def dfs(v, componente):
        visitados[v] = True
        componente.append(v)
        for u in grafo[v]:
            if not visitados[u]:
                dfs(u, componente)
    
    for i in range(n):
        if not visitados[i]:
            componente = []
            dfs(i, componente)
            componentes.append(componente)
    
    return componentes
```

## 8. Complejidad de Operaciones

| Operación | Matriz | Lista |
|-----------|--------|-------|
| Verificar arista | O(1) | O(grado) |
| Agregar arista | O(1) | O(1) |
| Eliminar arista | O(1) | O(grado) |
| BFS/DFS | O(V²) | O(V+E) |
| Espacio | O(V²) | O(V+E) |

## 9. Aplicaciones Comunes

- **GPS/Mapas**: Dijkstra para rutas
- **Redes Sociales**: Recomendaciones, análisis de comunidades
- **Compiladores**: Análisis de dependencias
- **Bases de datos**: Consultas relacionales
- **Videojuegos**: Pathfinding, IA
- **Biología**: Redes metabólicas
- **Logística**: Optimización de rutas

## 10. Consejos Prácticos

1. **Elige la representación sabiamente**
   - Grafo denso → Matriz de adyacencia
   - Grafo disperso → Lista de adyacencia

2. **BFS vs DFS**
   - BFS: Camino más corto en grafos no ponderados
   - DFS: Ciclos, topología, componentes conectadas

3. **Complejidad espacial**
   - Siempre considera la memoria requerida

4. **Validación**
   - Verifica que los vértices existan
   - Maneja grafos desconectados

5. **Debugging**
   - Dibuja el grafo
   - Traza manualmente el algoritmo
   - Usa visualizaciones
