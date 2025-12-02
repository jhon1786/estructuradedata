# Sitemap - Blog de Grafos

## Estructura del Proyecto

```
proyecto-grafos/
├── index.html              (Página principal con demo)
├── indice.html             (Índice/Home page)
├── bienvenida.html         (Página de bienvenida)
├── conceptos.html          (Conceptos fundamentales)
├── guia_rapida.html        (Referencia rápida - NO CREADA AÚN)
├── styles.css              (Estilos CSS principales)
├── script.js               (JavaScript principal)
├── config.json             (Configuración del sitio)
├── ejercicio.py            (Ejemplo de Cola - original)
├── grafo_ejemplos.py       (Ejemplos de Grafos)
├── test_grafo.py           (Tests unitarios)
├── guia_rapida.md          (Guía en Markdown)
├── sitemap.md              (Este archivo)
└── resumen.txt             (Resumen ejecutivo)
```

## Navegación del Sitio

### Nivel 1: Página Principal
- **index.html** → Demo interactiva principal
  - Tipos de grafos
  - Visualización
  - Matriz de adyacencia
  - Algoritmos

- **indice.html** → Home page / Índice
  - Acceso a todo el contenido
  - Plan de estudio
  - Mapa del sitio

### Nivel 2: Contenido Educativo
- **bienvenida.html** → Introducción
  - Por qué estudiar grafos
  - Qué aprenderás
  - Recursos disponibles

- **conceptos.html** → Teoría fundamental
  - Definición de grafos
  - Tipos de grafos
  - Representación
  - Propiedades

- **guia_rapida.html** → Referencia práctica
  - Algoritmos con código
  - Tablas de complejidad
  - Consejos prácticos

### Nivel 3: Código Python
- **ejercicio.py** → Ejemplo de Cola
  - Implementación básica
  - Ejemplos de uso

- **grafo_ejemplos.py** → Ejemplos de Grafos
  - Clase Grafo
  - BFS, DFS
  - Dijkstra
  - Aplicaciones reales

- **test_grafo.py** → Tests unitarios
  - Validación de implementación
  - Casos de prueba

## Páginas HTML

### index.html (Página Principal)
```
├── Navbar (navegación)
├── Hero Section
├── Sección: ¿Qué es un Grafo?
├── Sección: Tipos de Grafos
├── Sección: Aplicaciones
├── Sección: Demo Interactiva
│   ├── Matriz de Adyacencia
│   └── Visualización del Grafo
├── Sección: Algoritmos
└── Footer
```

### indice.html (Página de Inicio)
```
├── Navbar (navegación)
├── Hero Section (Bienvenida)
├── Contenido Principal (4 cards)
│   ├── Bienvenida
│   ├── Conceptos
│   ├── Guía Rápida
│   └── Demo
├── Código Python (2 sections)
│   ├── grafo_ejemplos.py
│   └── test_grafo.py
├── Mapa del Sitio
├── Plan de Estudio (6 pasos)
├── Configuración
└── Footer
```

### bienvenida.html (Página de Bienvenida)
```
├── Navbar (navegación)
├── Hero Section
├── Por qué estudiar Grafos (3 cards)
├── Lo que aprenderás (lista)
├── Cómo usar el blog (4 pasos)
├── Recursos Disponibles (3 grupos)
├── Botón de Acción
└── Footer
```

### conceptos.html (Conceptos Fundamentales)
```
├── Navbar (navegación)
├── Hero Section
├── Definición
├── Terminología Básica (6 términos)
├── Clasificación
│   ├── Por Dirección (2 tipos)
│   ├── Por Pesos (2 tipos)
│   ├── Por Ciclos (2 tipos)
│   └── Casos Especiales (2 tipos)
├── Representación en Memoria
├── Propiedades Importantes
└── Footer
```

## Archivos de Configuración

### config.json
```json
{
  "sitio": { metadata },
  "navegacion": { menus },
  "temas": [ { contenido } ],
  "ejemplos": { configuración },
  "estilos": { colores y tipografía },
  "performance": { cache, minificación }
}
```

### styles.css
Secciones:
- Reset y variables globales
- Navbar
- Hero sections
- Botones
- Grillas y cards
- Responsive design
- Animaciones

### script.js
Funcionalidades:
- Navegación suave (smooth scroll)
- Actualización de links activos
- Animaciones al scroll (IntersectionObserver)
- Clase Grafo (BFS, DFS, Dijkstra)

## Documentación

### guia_rapida.md
1. Conceptos clave
2. Tipos de grafos
3. Representación
4. Algoritmos BFS/DFS
5. Algoritmos de camino corto
6. Detección de ciclos
7. Componentes conectadas
8. Tabla de complejidades
9. Aplicaciones
10. Consejos prácticos

### sitemap.md (Este archivo)
- Estructura completa del proyecto
- Navegación del sitio
- Contenido de cada página

### resumen.txt
- Resumen ejecutivo
- Descripción general
- Características
- Instrucciones de ejecución

## Flujos de Navegación

### Flujo Recomendado para Estudiantes
1. index.html (Demo)
   ↓
2. indice.html (Home)
   ↓
3. bienvenida.html (Introducción)
   ↓
4. conceptos.html (Teoría)
   ↓
5. guia_rapida.html (Referencia)
   ↓
6. Ejecutar grafo_ejemplos.py
   ↓
7. Ejecutar test_grafo.py

### Flujo Rápido para Referencia
1. indice.html
   ↓
2. guia_rapida.html
   ↓
3. config.json (para valores específicos)

## Recursos Externos

### Enlaces del Sitio
- Dentro de cada página HTML hay links a:
  - Otras páginas HTML
  - Secciones internas (#id)
  - Archivos de código Python

### Relaciones Entre Archivos
```
index.html ←→ styles.css ← script.js ← config.json
indice.html ←→ styles.css ← script.js
bienvenida.html ←→ styles.css ← script.js
conceptos.html ←→ styles.css ← script.js

grafo_ejemplos.py → Demostración de código
test_grafo.py → Validación de grafo_ejemplos.py
ejercicio.py → Base original del proyecto
```

## Ejecución

### Para Navegar el Blog
```bash
# Opción 1: Servidor Python
python -m http.server 8000
# Visitar http://localhost:8000

# Opción 2: Abrir directamente
# Abrir index.html en el navegador
```

### Para Ejecutar Código Python
```bash
# Ejemplos
python grafo_ejemplos.py

# Tests
python test_grafo.py

# Ejercicio original
python ejercicio.py
```

## Meta Information

| Propiedad | Valor |
|-----------|-------|
| Nombre | Blog de Estructura de Datos - Grafos |
| Versión | 1.0 |
| Idioma | Español |
| Páginas HTML | 5 |
| Archivos Python | 3 |
| Archivos CSS | 1 |
| Archivos JS | 1 |
| Archivos JSON | 1 |
| Archivos MD | 2 |
| Archivos TXT | 1 |
| **TOTAL** | **15 archivos** |

---

**Última actualización**: Diciembre 2025
**Estado**: Completo
