# Portafolio de Programación - Matemáticas Aplicadas



## Información Personal

**Nombre:** Miller Alexander Quiroga Campos  
**Carrera:** Pregrado en Matemáticas Aplicadas  
**Semestre:** Primero (2025)  
**Universidad:** Universidad Colegio Mayor de Cundinamarca  

> "Las matemáticas no mienten, lo que hay son muchos matemáticos mentirosos." — Henry David Thoreau

## Tabla de Contenidos
- [Sobre Mí](#sobre-mí)
- [Objetivos de Aprendizaje](#objetivos-de-aprendizaje)
- [Proyectos](#proyectos)
- [Habilidades Técnicas](#habilidades-técnicas)
- [Bitácora de Aprendizaje](#bitácora-de-aprendizaje)
- [Recursos y Referencias](#recursos-y-referencias)
- [Contacto](#contacto)

## Sobre Mí

Soy estudiante de primer semestre de Matemáticas Aplicadas con interés particular en modelación matemática y ciencia de datos. Desde pequeña he tenido fascinación por resolver problemas lógicos y encontrar patrones en datos. Elegí esta carrera porque combina mi pasión por las matemáticas con aplicaciones prácticas en el mundo real.

## Objetivos de Aprendizaje

- Dominar los fundamentos de programación estructurada
- Aprender a implementar algoritmos matemáticos en código
- Desarrollar habilidades de pensamiento computacional
- Familiarizarme con el control de versiones usando Git y GitHub
- Adquirir bases sólidas para futuros cursos de programación orientada a objetos

## Proyectos

### 1. Calculadora de Matrices
**Descripción:** Implementación de operaciones básicas con matrices (suma, resta, multiplicación, determinante).  
**Conceptos aplicados:** Álgebra lineal, programación modular  
**Tecnologías:** Python, NumPy  
**Estado:** Completado  
**Enlace:** [/proyectos/calculadora_matrices](/proyectos/calculadora_matrices)

```python
# Ejemplo de código para multiplicación de matrices
def multiplicar_matrices(A, B):
    if len(A[0]) != len(B):
        raise ValueError("Dimensiones incompatibles para multiplicación")
    
    resultado = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                resultado[i][j] += A[i][k] * B[k][j]
    
    return resultado
```

### 2. Métodos Numéricos
**Descripción:** Colección de implementaciones de métodos numéricos para resolución de ecuaciones.  
**Conceptos aplicados:** Cálculo, aproximación numérica  
**Tecnologías:** Python, Matplotlib  
**Estado:** En progreso  
**Enlace:** [/proyectos/metodos_numericos](/proyectos/metodos_numericos)

#### Avance actual:
- [x] Método de bisección
- [x] Método de Newton-Raphson
- [ ] Método de la secante
- [ ] Integración numérica

## Habilidades Técnicas

| Habilidad | Nivel |
|-----------|-------|
| Python | ⭐⭐⭐☆☆ |
| Git/GitHub | ⭐⭐☆☆☆ |
| Markdown | ⭐⭐⭐☆☆ |
| LaTeX | ⭐⭐☆☆☆ |
| NumPy | ⭐⭐☆☆☆ |
| Matplotlib | ⭐⭐☆☆☆ |

## Bitácora de Aprendizaje

### Semana 1 (15-19 Marzo, 2025)
Aprendí los conceptos básicos de programación en Python: variables, tipos de datos, estructuras de control y funciones. Realicé ejercicios simples como calcular factorial y secuencia de Fibonacci.

### Semana 2 (22-26 Marzo, 2025)
Introducción a Git y GitHub. Creé mi primer repositorio y aprendí comandos básicos (commit, push, pull). Comencé a documentar mi código utilizando docstrings en Python.

## Recursos y Referencias

- Libro: "Introducción a la Programación con Python" - Autor: J. Fernández
- Curso online: "Git & GitHub para principiantes" - Plataforma Coursera
- Documentación oficial de Python: [python.org](https://docs.python.org/3/)
- Tutoriales de NumPy: [numpy.org](https://numpy.org/doc/stable/user/tutorials_index.html)

## Contacto

📧 Email: malexanderquiroga@unicolmayor.edu.co  
🔗 GitHub: [MillerSamqC](https://github.com/millersamqc)  
🔗 LinkedIn: [Miller Quiroga Campos](https://linkedin.com/in/Miller
