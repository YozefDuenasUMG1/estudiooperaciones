# Estudio de Operaciones - Operations Research Solver

Este repositorio contiene implementaciones de métodos clásicos de investigación de operaciones para resolver problemas de transporte y asignación.

## 🚀 Características

- **Problema de Transporte**:
  - Método del Costo Mínimo
  - Método de Aproximación de Vogel (VAM)
  - Balanceado automático de problemas no balanceados

- **Problema de Asignación**:
  - Método Húngaro (Hungarian Method)
  - Manejo automático de matrices no cuadradas

## 📋 Requisitos

```bash
pip install -r requirements.txt
```

## 🎯 Uso

### 1. Ejecutar Ejemplos Predefinidos

```bash
python operations_research_solver.py
```

### 2. Interfaz Interactiva

```bash
python interactive_solver.py
```

## 📝 Ejemplos

### Problema de Transporte

```python
from operations_research_solver import TransportationProblem

# Matriz de costos (3 proveedores x 4 destinos)
costs = [
    [8, 6, 10, 9],
    [9, 12, 13, 7],
    [14, 9, 16, 5]
]
supply = [20, 30, 25]    # Capacidad de suministro
demand = [15, 20, 15, 25]  # Demanda requerida

tp = TransportationProblem(costs, supply, demand)

# Método del Costo Mínimo
allocation1, cost1 = tp.minimum_cost_method()

# Método de Vogel
allocation2, cost2 = tp.vogel_approximation_method()
```

### Problema de Asignación

```python
from operations_research_solver import AssignmentProblem

# Matriz de costos (4 trabajadores x 4 tareas)
costs = [
    [9, 2, 7, 8],
    [6, 4, 3, 7],
    [5, 8, 1, 8],
    [7, 6, 9, 4]
]

ap = AssignmentProblem(costs)
assignments, total_cost = ap.hungarian_method()
```

## 🔧 Métodos Implementados

### 1. Método del Costo Mínimo
- Selecciona la celda con menor costo disponible
- Asigna la máxima cantidad posible
- Continúa hasta satisfacer toda la oferta y demanda

### 2. Método de Aproximación de Vogel (VAM)
- Calcula penalidades para filas y columnas
- Selecciona la fila/columna con mayor penalidad
- Asigna en la celda de menor costo de esa fila/columna
- Generalmente produce mejores soluciones iniciales

### 3. Método Húngaro
- Reducción de filas y columnas
- Cobertura de ceros con líneas mínimas
- Creación de ceros adicionales si es necesario
- Encuentra la asignación óptima

## 📊 Resultados de Ejemplo

### Problema de Transporte
```
Método del Costo Mínimo: $575.00
Método de Vogel: $575.00
```

### Problema de Asignación
```
Trabajador 1 → Tarea 2 (Costo: $2.00)
Trabajador 2 → Tarea 1 (Costo: $6.00)
Trabajador 3 → Tarea 3 (Costo: $1.00)
Trabajador 4 → Tarea 4 (Costo: $4.00)
Costo Total: $13.00
```

## 📚 Documentación Incluida

El repositorio incluye documentos de referencia:
- `PROBLEMAS DE TRANSPORTE Y ASIGNACION.pdf`
- `metodo-aproximacion-vogel.pdf`
- `costo-minimo.pdf`
- `FORMULACION_DEL_PROBLEMA_DE_ASIGNACION_M.pdf`
- `Semana 9 metodo hungaro.xlsx`

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Por favor:
1. Haz fork del repositorio
2. Crea una rama para tu feature
3. Realiza tus cambios
4. Envía un pull request

## 📄 Licencia

Este proyecto está bajo la Licencia MIT.