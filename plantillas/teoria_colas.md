# Plantilla: Teoría de Colas

## Definición del Sistema
**Descripción:** [Descripción del sistema de espera]

**Características del Sistema:**
- **Patrón de llegadas:** [Poisson/Constante/Otro]
- **Patrón de servicio:** [Exponencial/Constante/Otro]
- **Número de servidores:** [s]
- **Capacidad del sistema:** [Finita/Infinita]
- **Disciplina de la cola:** [FIFO/LIFO/Prioridad]
- **Población de usuarios:** [Finita/Infinita]

## Notación de Kendall
**Modelo:** A/B/s/N/K/SD

Donde:
- A = Distribución de llegadas
- B = Distribución de servicio
- s = Número de servidores
- N = Capacidad del sistema
- K = Tamaño de la población
- SD = Disciplina de servicio

## Parámetros del Sistema
- **Tasa de llegadas (λ):** [valor] clientes/unidad de tiempo
- **Tasa de servicio (μ):** [valor] clientes/unidad de tiempo por servidor
- **Factor de utilización (ρ):** ρ = λ/(sμ) = [valor]

## Análisis del Estado Estacionario
**Condición de estabilidad:** ρ < 1 ✓/✗

**Medidas de Desempeño:**
- **L:** Número promedio de clientes en el sistema = [valor]
- **Lq:** Número promedio de clientes en cola = [valor]
- **W:** Tiempo promedio en el sistema = [valor]
- **Wq:** Tiempo promedio en cola = [valor]
- **P₀:** Probabilidad de que el sistema esté vacío = [valor]
- **Pₙ:** Probabilidad de n clientes en el sistema = [fórmula]

## Costos del Sistema (si aplica)
- **Costo de espera:** [valor] por unidad de tiempo por cliente
- **Costo de servicio:** [valor] por servidor por unidad de tiempo
- **Costo total esperado:** CT = CwL + CsS = [valor]

## Interpretación de Resultados
[Análisis de los resultados y recomendaciones]