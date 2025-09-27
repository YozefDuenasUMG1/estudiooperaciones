# Solución: Problema de Producción

## Definición del Problema

**Variables de Decisión:**
- x₁ = número de productos A a producir
- x₂ = número de productos B a producir

## Modelo Matemático

**Función Objetivo:**
Maximizar: Z = 30x₁ + 20x₂

**Restricciones:**
1. Tiempo de máquina: 2x₁ + x₂ ≤ 100
2. Tiempo de mano de obra: x₁ + 2x₂ ≤ 80
3. No negatividad: x₁, x₂ ≥ 0

## Solución Gráfica

### Paso 1: Graficar las restricciones

**Restricción 1:** 2x₁ + x₂ ≤ 100
- Si x₁ = 0: x₂ = 100
- Si x₂ = 0: x₁ = 50
- Puntos: (0, 100) y (50, 0)

**Restricción 2:** x₁ + 2x₂ ≤ 80
- Si x₁ = 0: x₂ = 40
- Si x₂ = 0: x₁ = 80
- Puntos: (0, 40) y (80, 0)

### Paso 2: Identificar la región factible
La región factible está limitada por:
- x₁ ≥ 0, x₂ ≥ 0
- 2x₁ + x₂ ≤ 100
- x₁ + 2x₂ ≤ 80

### Paso 3: Encontrar puntos extremos
1. Origen: (0, 0)
2. Intersección con eje x₁: (50, 0) - solo considerando restricción 1
3. Intersección con eje x₂: (0, 40) - restricción 2 es más limitante
4. Intersección de las dos restricciones:
   - 2x₁ + x₂ = 100
   - x₁ + 2x₂ = 80
   
   Resolviendo el sistema:
   - De la segunda: x₁ = 80 - 2x₂
   - Sustituyendo: 2(80 - 2x₂) + x₂ = 100
   - 160 - 4x₂ + x₂ = 100
   - -3x₂ = -60
   - x₂ = 20, x₁ = 40
   
   Punto: (40, 20)

### Paso 4: Evaluar la función objetivo
1. En (0, 0): Z = 30(0) + 20(0) = $0
2. En (50, 0): Z = 30(50) + 20(0) = $1,500
3. En (0, 40): Z = 30(0) + 20(40) = $800
4. En (40, 20): Z = 30(40) + 20(20) = $1,200 + $400 = $1,600

## Solución Óptima

**Valores óptimos:**
- x₁ = 40 productos A
- x₂ = 20 productos B
- Ganancia máxima: Z = $1,600

## Verificación
**Restricción 1:** 2(40) + 20 = 80 + 20 = 100 ≤ 100 ✓
**Restricción 2:** 40 + 2(20) = 40 + 40 = 80 ≤ 80 ✓

## Análisis de Recursos
- **Tiempo de máquina:** 100 horas utilizadas (100% utilización)
- **Tiempo de mano de obra:** 80 horas utilizadas (100% utilización)
- Ambos recursos están completamente utilizados (restricciones activas)

## Interpretación
La empresa debe producir 40 unidades del producto A y 20 unidades del producto B para obtener la ganancia máxima de $1,600, utilizando completamente ambos recursos disponibles.