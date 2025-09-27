# Plantilla: Problema de Transporte

## Definición del Problema
**Descripción:** [Descripción del problema de transporte]

**Datos del Problema:**
- **Orígenes (Fuentes):** [O₁, O₂, ..., Oₘ]
- **Destinos:** [D₁, D₂, ..., Dₙ]
- **Ofertas:** [s₁, s₂, ..., sₘ]
- **Demandas:** [d₁, d₂, ..., dₙ]

## Tabla de Costos
|        | D₁  | D₂  | ... | Dₙ  | Oferta |
|--------|-----|-----|-----|-----|--------|
| **O₁** | c₁₁ | c₁₂ | ... | c₁ₙ | s₁     |
| **O₂** | c₂₁ | c₂₂ | ... | c₂ₙ | s₂     |
| ...    | ... | ... | ... | ... | ...    |
| **Oₘ** | cₘ₁ | cₘ₂ | ... | cₘₙ | sₘ     |
|**Demanda**| d₁ | d₂  | ... | dₙ  | Total  |

## Verificación de Balance
- Oferta Total: Σsᵢ = [valor]
- Demanda Total: Σdⱼ = [valor]
- Estado: [Balanceado/Desbalanceado]

## Método de Solución
### Solución Inicial
- [ ] Método de la Esquina Noroeste
- [ ] Método del Costo Mínimo
- [ ] Método de Vogel (VAM)

### Optimización
- [ ] Método MODI (u-v)
- [ ] Método de Stepping Stone

## Análisis de Degeneración
- Número de variables básicas requeridas: m + n - 1 = [valor]
- Variables básicas en la solución: [número]
- Estado: [No degenerado/Degenerado]

## Solución Óptima
**Asignaciones:**
- xᵢⱼ = [cantidad] (de Oᵢ a Dⱼ)

**Costo Total:** Z = [valor]