"""
TESTS UNITARIOS PARA LA CLASE GRAFO
Valida la implementación de grafos y sus algoritmos
"""

import unittest
from grafo_ejemplos import Grafo


class TestGrafo(unittest.TestCase):
    """Tests para la clase Grafo"""
    
    def setUp(self):
        """Se ejecuta antes de cada test"""
        self.grafo = Grafo(dirigido=False)
        self.grafo_dirigido = Grafo(dirigido=True)
    
    # Tests de Creación y Aristas
    
    def test_grafo_vacio(self):
        """Test: Grafo vacío no tiene vértices"""
        self.assertEqual(len(self.grafo.grafo), 0)
    
    def test_agregar_arista_simple(self):
        """Test: Agregar una arista simple"""
        self.grafo.agregar_arista('A', 'B')
        self.assertIn('A', self.grafo.grafo)
        self.assertIn('B', self.grafo.grafo)
    
    def test_agregar_multiples_aristas(self):
        """Test: Agregar múltiples aristas"""
        aristas = [('A', 'B'), ('B', 'C'), ('C', 'D')]
        for u, v in aristas:
            self.grafo.agregar_arista(u, v)
        
        self.assertEqual(len(self.grafo.grafo), 4)
    
    def test_arista_ponderada(self):
        """Test: Agregar arista con peso"""
        self.grafo.agregar_arista('A', 'B', peso=5)
        vecinos = self.grafo.grafo['A']
        self.assertEqual(len(vecinos), 1)
        self.assertEqual(vecinos[0], ('B', 5))
    
    def test_grafo_no_dirigido_simetrico(self):
        """Test: Grafo no dirigido es simétrico"""
        self.grafo.agregar_arista('A', 'B')
        
        # Verificar que existe en ambas direcciones
        vecinos_a = [v for v, _ in self.grafo.grafo['A']]
        vecinos_b = [v for v, _ in self.grafo.grafo['B']]
        
        self.assertIn('B', vecinos_a)
        self.assertIn('A', vecinos_b)
    
    def test_grafo_dirigido_asimetrico(self):
        """Test: Grafo dirigido es asimétrico"""
        self.grafo_dirigido.agregar_arista('A', 'B')
        
        # Verificar dirección
        vecinos_a = [v for v, _ in self.grafo_dirigido.grafo['A']]
        vecinos_b = [v for v, _ in self.grafo_dirigido.grafo.get('B', [])]
        
        self.assertIn('B', vecinos_a)
        self.assertEqual(len(vecinos_b), 0)
    
    # Tests de BFS
    
    def test_bfs_vertice_unico(self):
        """Test: BFS en grafo con un solo vértice"""
        self.grafo.agregar_arista('A', 'A')  # Auto-loop
        resultado = self.grafo.bfs('A')
        self.assertEqual(resultado, ['A'])
    
    def test_bfs_orden_correcto(self):
        """Test: BFS retorna orden correcto"""
        aristas = [('A', 'B'), ('A', 'C'), ('B', 'D'), ('C', 'D')]
        for u, v in aristas:
            self.grafo.agregar_arista(u, v)
        
        resultado = self.grafo.bfs('A')
        
        # A debe ser primero
        self.assertEqual(resultado[0], 'A')
        
        # B y C deben estar antes que D
        self.assertTrue(resultado.index('B') < resultado.index('D'))
        self.assertTrue(resultado.index('C') < resultado.index('D'))
    
    def test_bfs_grafo_desconectado(self):
        """Test: BFS en grafo desconectado"""
        # Componente 1
        self.grafo.agregar_arista('A', 'B')
        # Componente 2 (sin conexión)
        self.grafo.agregar_arista('C', 'D')
        
        resultado = self.grafo.bfs('A')
        
        # BFS desde A no alcanza C ni D
        self.assertNotIn('C', resultado)
        self.assertNotIn('D', resultado)
    
    # Tests de DFS
    
    def test_dfs_vertice_unico(self):
        """Test: DFS en grafo con un solo vértice"""
        self.grafo.agregar_arista('A', 'A')
        resultado = self.grafo.dfs('A')
        self.assertEqual(resultado, ['A'])
    
    def test_dfs_retorna_todos_vertices(self):
        """Test: DFS retorna todos los vértices conectados"""
        aristas = [('A', 'B'), ('B', 'C'), ('C', 'D')]
        for u, v in aristas:
            self.grafo.agregar_arista(u, v)
        
        resultado = self.grafo.dfs('A')
        self.assertEqual(set(resultado), {'A', 'B', 'C', 'D'})
    
    def test_dfs_sin_repeticion(self):
        """Test: DFS no repite vértices"""
        self.grafo.agregar_arista('A', 'B')
        self.grafo.agregar_arista('B', 'A')  # Ciclo
        
        resultado = self.grafo.dfs('A')
        self.assertEqual(len(resultado), len(set(resultado)))
    
    # Tests de Dijkstra
    
    def test_dijkstra_vertice_unico(self):
        """Test: Dijkstra en grafo con un vértice"""
        self.grafo.agregar_arista('A', 'A', peso=0)
        distancias = self.grafo.dijkstra('A')
        self.assertEqual(distancias['A'], 0)
    
    def test_dijkstra_distancia_inicio_cero(self):
        """Test: Distancia del inicio es siempre 0"""
        self.grafo.agregar_arista('A', 'B', peso=5)
        distancias = self.grafo.dijkstra('A')
        self.assertEqual(distancias['A'], 0)
    
    def test_dijkstra_camino_directo(self):
        """Test: Dijkstra camino directo"""
        self.grafo.agregar_arista('A', 'B', peso=3)
        distancias = self.grafo.dijkstra('A')
        self.assertEqual(distancias['B'], 3)
    
    def test_dijkstra_camino_indirecto(self):
        """Test: Dijkstra elige camino más corto"""
        # Camino 1: A-B-C (3+2=5)
        self.grafo.agregar_arista('A', 'B', peso=3)
        self.grafo.agregar_arista('B', 'C', peso=2)
        # Camino 2: A-C directo (10)
        self.grafo.agregar_arista('A', 'C', peso=10)
        
        distancias = self.grafo.dijkstra('A')
        
        # Debe elegir el camino de 5, no el de 10
        self.assertEqual(distancias['C'], 5)
    
    def test_dijkstra_retorna_diccionario(self):
        """Test: Dijkstra retorna un diccionario"""
        self.grafo.agregar_arista('A', 'B', peso=1)
        distancias = self.grafo.dijkstra('A')
        
        self.assertIsInstance(distancias, dict)
        self.assertIn('A', distancias)
        self.assertIn('B', distancias)
    
    # Tests de Casos Especiales
    
    def test_vertices_no_existentes(self):
        """Test: Manejar vértices no existentes"""
        self.grafo.agregar_arista('A', 'B')
        
        # Dijkstra debe crear entrada para todos los vértices
        distancias = self.grafo.dijkstra('A')
        self.assertIn('A', distancias)
        self.assertIn('B', distancias)
    
    def test_aristas_negativas_dijkstra(self):
        """Test: Dijkstra con aristas negativas (no recomendado)"""
        # Dijkstra no está diseñado para pesos negativos
        # Este test documenta el comportamiento
        self.grafo.agregar_arista('A', 'B', peso=-1)
        distancias = self.grafo.dijkstra('A')
        
        # Esperamos comportamiento indefinido, pero no crash
        self.assertIsInstance(distancias, dict)
    
    def test_grafo_completo(self):
        """Test: Grafo completo (todos conectados con todos)"""
        vertices = ['A', 'B', 'C']
        
        for i, u in enumerate(vertices):
            for v in vertices[i+1:]:
                self.grafo.agregar_arista(u, v)
        
        resultado_bfs = self.grafo.bfs('A')
        self.assertEqual(set(resultado_bfs), set(vertices))
    
    # Tests de Performance
    
    def test_bfs_grafo_grande(self):
        """Test: BFS en grafo grande"""
        # Crear grafo lineal: 0-1-2-...-99
        for i in range(99):
            self.grafo.agregar_arista(i, i+1)
        
        resultado = self.grafo.bfs(0)
        
        # Debe contener todos los vértices
        self.assertEqual(len(resultado), 100)
    
    def test_dfs_grafo_profundo(self):
        """Test: DFS en grafo profundo"""
        # Crear grafo lineal profundo
        for i in range(99):
            self.grafo_dirigido.agregar_arista(i, i+1)
        
        resultado = self.grafo_dirigido.dfs(0)
        
        # Debe alcanzar el final
        self.assertIn(99, resultado)
    
    # Tests de Correctitud
    
    def test_bfs_dfs_mismos_vertices(self):
        """Test: BFS y DFS visitan los mismos vértices en grafo conectado"""
        aristas = [('A', 'B'), ('B', 'C'), ('C', 'D')]
        for u, v in aristas:
            self.grafo.agregar_arista(u, v)
        
        resultado_bfs = set(self.grafo.bfs('A'))
        resultado_dfs = set(self.grafo.dfs('A'))
        
        self.assertEqual(resultado_bfs, resultado_dfs)
    
    def test_ciclo_en_grafo(self):
        """Test: Manejo de ciclos"""
        # Crear ciclo: A-B-C-A
        self.grafo.agregar_arista('A', 'B')
        self.grafo.agregar_arista('B', 'C')
        self.grafo.agregar_arista('C', 'A')
        
        # BFS debe terminar (sin ciclo infinito)
        resultado = self.grafo.bfs('A')
        self.assertEqual(len(resultado), 3)


class TestIntegracion(unittest.TestCase):
    """Tests de integración"""
    
    def test_flujo_completo(self):
        """Test: Flujo completo de creación y análisis"""
        # Crear grafo
        g = Grafo(dirigido=False)
        
        # Agregar aristas
        aristas = [('A', 'B', 1), ('B', 'C', 2), ('A', 'C', 5)]
        for u, v, w in aristas:
            g.agregar_arista(u, v, w)
        
        # BFS
        bfs_resultado = g.bfs('A')
        self.assertEqual(set(bfs_resultado), {'A', 'B', 'C'})
        
        # DFS
        dfs_resultado = g.dfs('A')
        self.assertEqual(set(dfs_resultado), {'A', 'B', 'C'})
        
        # Dijkstra
        distancias = g.dijkstra('A')
        self.assertEqual(distancias['A'], 0)
        self.assertEqual(distancias['B'], 1)
        self.assertEqual(distancias['C'], 3)  # A-B-C (1+2=3)


def main():
    """Ejecuta todos los tests"""
    # Crear suite de tests
    suite = unittest.TestLoader().loadTestsFromModule(__import__(__name__))
    
    # Ejecutar con verbosidad
    runner = unittest.TextTestRunner(verbosity=2)
    resultado = runner.run(suite)
    
    # Retornar código de salida
    return 0 if resultado.wasSuccessful() else 1


if __name__ == '__main__':
    unittest.main(verbosity=2)
