// Navegación suave
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            target.scrollIntoView({
                behavior: 'smooth',
                block: 'start'
            });
            // Actualizar enlace activo
            document.querySelectorAll('.nav-menu a').forEach(a => a.classList.remove('active'));
            this.classList.add('active');
        }
    });
});

// Actualizar enlace activo al hacer scroll
window.addEventListener('scroll', () => {
    let current = '';
    const sections = document.querySelectorAll('section[id]');
    
    sections.forEach(section => {
        const sectionTop = section.offsetTop;
        const sectionHeight = section.clientHeight;
        if (pageYOffset >= sectionTop - 200) {
            current = section.getAttribute('id');
        }
    });
    
    document.querySelectorAll('.nav-menu a').forEach(a => {
        a.classList.remove('active');
        if (a.getAttribute('href').includes(current)) {
            a.classList.add('active');
        }
    });
});

// Función para hacer scroll a una sección
function scrollToSection(sectionId) {
    const section = document.getElementById(sectionId);
    if (section) {
        section.scrollIntoView({
            behavior: 'smooth',
            block: 'start'
        });
    }
}

// Animación de elementos al entrar en viewport
const observerOptions = {
    threshold: 0.1,
    rootMargin: '0px 0px -100px 0px'
};

const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.style.animation = 'fadeInUp 0.6s ease forwards';
            observer.unobserve(entry.target);
        }
    });
}, observerOptions);

// Observar todos los cards
document.querySelectorAll('.card, .app-item, .algo-card').forEach(el => {
    observer.observe(el);
});

// Clase para representar un Grafo (ejemplo práctico)
class Grafo {
    constructor() {
        this.vertices = [];
        this.adyacencia = new Map();
    }
    
    agregarVertice(vertice) {
        if (!this.adyacencia.has(vertice)) {
            this.vertices.push(vertice);
            this.adyacencia.set(vertice, []);
        }
    }
    
    agregarArista(v1, v2, dirigido = false) {
        if (!this.adyacencia.has(v1)) {
            this.agregarVertice(v1);
        }
        if (!this.adyacencia.has(v2)) {
            this.agregarVertice(v2);
        }
        
        this.adyacencia.get(v1).push(v2);
        if (!dirigido) {
            this.adyacencia.get(v2).push(v1);
        }
    }
    
    bfs(inicio) {
        const visitados = new Set();
        const cola = [inicio];
        const resultado = [];
        
        visitados.add(inicio);
        
        while (cola.length > 0) {
            const vertice = cola.shift();
            resultado.push(vertice);
            
            for (let vecino of this.adyacencia.get(vertice)) {
                if (!visitados.has(vecino)) {
                    visitados.add(vecino);
                    cola.push(vecino);
                }
            }
        }
        
        return resultado;
    }
    
    dfs(inicio) {
        const visitados = new Set();
        const resultado = [];
        
        const _dfs = (vertice) => {
            visitados.add(vertice);
            resultado.push(vertice);
            
            for (let vecino of this.adyacencia.get(vertice)) {
                if (!visitados.has(vecino)) {
                    _dfs(vecino);
                }
            }
        };
        
        _dfs(inicio);
        return resultado;
    }
}

// Ejemplo de uso
const grafo = new Grafo();
grafo.agregarArista('A', 'B');
grafo.agregarArista('A', 'D');
grafo.agregarArista('B', 'C');
grafo.agregarArista('C', 'D');

console.log('BFS desde A:', grafo.bfs('A'));
console.log('DFS desde A:', grafo.dfs('A'));

// Información del grafo en consola
console.log('Información del Grafo:');
console.log('Vértices:', grafo.vertices);
console.log('Adyacencias:', Object.fromEntries(grafo.adyacencia));
