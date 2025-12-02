# Blog de Estructura de Datos: Grafos

## Descripción
Blog educativo completo sobre grafos - una de las estructuras de datos más importantes en programación. Incluye teoría, ejemplos prácticos, código Python y visualizaciones interactivas.

## 📁 Estructura del Proyecto

```
proyecto-grafos/
├── HTML (Páginas del Blog)
│   ├── index.html              - Página principal con demo interactiva
│   ├── indice.html             - Índice/Home page
│   ├── bienvenida.html         - Página de bienvenida
│   ├── conceptos.html          - Conceptos fundamentales
│   └── guia_rapida.html        - Guía rápida de referencia
│
├── Python (Código Ejecutable)
│   ├── ejercicio.py            - Ejemplo original de Cola (Queue)
│   ├── grafo_ejemplos.py       - Ejemplos de Grafos
│   └── test_grafo.py           - Tests unitarios
│
├── Web (Estilos y Scripts)
│   ├── styles.css              - Estilos CSS
│   ├── script.js               - JavaScript interactivo
│   └── config.json             - Configuración del sitio
│
├── Documentación
│   ├── guia_rapida.md          - Guía en Markdown
│   ├── sitemap.md              - Mapa del sitio
│   └── resumen.txt             - Resumen ejecutivo
│
└── README.md                    - Este archivo
```

## 🚀 Cómo Usar

### Opción 1: Ver el Blog (Recomendado)

Abre cualquiera de estos archivos en tu navegador:
- `index.html` - Demo interactiva
- `indice.html` - Página de inicio

O sirve los archivos con un servidor HTTP:

```bash
# Python 3
python -m http.server 8000

# Node.js
npx http-server

# Luego abre http://localhost:8000
```

### Opción 2: Ejecutar el Código Python

```bash
# Ver ejemplos de grafos
python grafo_ejemplos.py

# Ejecutar tests unitarios
python test_grafo.py

# Ver el ejemplo original de Cola
python ejercicio.py
```

## 📚 Contenido

### Páginas HTML
- **Bienvenida** (`bienvenida.html`) - Introducción y motivación
- **Conceptos** (`conceptos.html`) - Definición, tipos, representación y propiedades
- **Guía Rápida** (`guia_rapida.html`) - Algoritmos con código y tablas de complejidad
- **Demo** (`index.html`) - Visualización interactiva de grafos
- **Índice** (`indice.html`) - Mapa completo del contenido

### Código Python

#### grafo_ejemplos.py
Implementación completa de grafos con:
- Clase `Grafo` (dirigido/no dirigido)
- Algoritmo BFS
- Algoritmo DFS
- Algoritmo de Dijkstra
- 5 ejemplos prácticos

#### test_grafo.py
Suite de tests incluyendo:
- Tests de creación
- Tests de aristas
- Tests de BFS/DFS
- Tests de Dijkstra
- Tests de casos especiales
- Tests de performance

## 🎯 Algoritmos Incluidos

| Algoritmo | Complejidad | Uso |
|-----------|-------------|-----|
| BFS | O(V + E) | Camino más corto (no ponderado) |
| DFS | O(V + E) | Ciclos, topología |
| Dijkstra | O(V²) o O((V+E)logV) | Camino más corto (ponderado) |

## 💡 Características

✅ **Teoría Completa** - Definiciones, tipos y propiedades  
✅ **Algoritmos** - BFS, DFS, Dijkstra y más  
✅ **Código Python** - Implementación funcional  
✅ **Tests Unitarios** - Validación automática  
✅ **Demo Interactiva** - Visualización en navegador  
✅ **Documentación** - Guías y referencias  
✅ **Ejemplos Prácticos** - Red social, mapas, etc.  
✅ **Diseño Responsivo** - Compatible con dispositivos  

## 🎓 Público Objetivo

- Estudiantes de Ciencias de la Computación
- Desarrolladores preparándose para entrevistas
- Cualquiera interesado en aprender algoritmos
- Profesores de estructuras de datos

## ⏱️ Tiempo de Estudio Estimado

- Lectura teórica: 1-2 horas
- Código y ejemplos: 1-2 horas
- Práctica: 2-3 horas
- **Total**: 4-7 horas

## 📋 Plan de Estudio Recomendado

1. **Comienza con Bienvenida** (5-10 min)
2. **Lee Conceptos** (15-20 min)
3. **Consulta Guía Rápida** (20-30 min)
4. **Ejecuta grafo_ejemplos.py** (10-15 min)
5. **Explora Demo Interactiva** (15-20 min)
6. **Ejecuta test_grafo.py** (10-15 min)

## 📖 Recursos

- **Conceptos Fundamentales**: `conceptos.html`
- **Referencia Rápida**: `guia_rapida.md` o `guia_rapida.html`
- **Implementación**: `grafo_ejemplos.py`
- **Tests**: `test_grafo.py`
- **Mapa Completo**: `sitemap.md`

## 🔧 Requisitos

**Software:**
- Navegador web moderno (Chrome, Firefox, Edge, Safari)
- Python 3.6+ (para ejecutar código)

**Conocimientos:**
- Python básico
- Conceptos fundamentales de programación
- Lógica de algoritmos

## 📝 Notas Importantes

- El blog es completamente offline - no requiere conexión a internet
- Todos los estilos están en `styles.css`
- La interactividad está en `script.js`
- La configuración está en `config.json`

## 🎨 Características del Diseño

- Gradientes modernos
- Animaciones suaves
- Navegación intuitiva
- Tema oscuro y claro compatible
- Totalmente responsivo

## 🐛 Troubleshooting

**El blog no se ve bien:**
- Abre en un navegador moderno (Chrome, Firefox, Edge)
- Limpia el caché del navegador

**No puedo ejecutar Python:**
- Asegúrate de tener Python 3.6+ instalado
- Verifica que está en tu PATH

**Los links no funcionan:**
- Asegúrate de tener todos los archivos HTML en la misma carpeta

## 📞 Soporte

Para más información:
- Consulta `resumen.txt` para un resumen ejecutivo
- Consulta `sitemap.md` para el mapa completo del sitio
- Revisa el código con comentarios en `grafo_ejemplos.py`

## 📄 Licencia

Este proyecto es educativo y está disponible para uso libre.

---

**Creado**: Diciembre 2025  
**Versión**: 1.0  
**Idioma**: Español  
**Archivos Totales**: 16
