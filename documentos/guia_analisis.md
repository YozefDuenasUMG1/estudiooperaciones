# Guía para Análisis de Ejercicios de Investigación de Operaciones

## Metodología de Análisis

### 1. Lectura y Comprensión
- **Leer cuidadosamente** el enunciado completo
- **Identificar** el contexto del problema (producción, transporte, inventarios, etc.)
- **Subrayar** datos numéricos importantes
- **Identificar** qué se pregunta exactamente

### 2. Clasificación del Problema

#### Palabras Clave por Tipo de Problema:

**Programación Lineal:**
- "maximizar", "minimizar"
- "función objetivo", "ganancia", "costo"
- "restricciones", "recursos limitados"
- "variables de decisión"

**Problemas de Transporte:**
- "distribuir", "enviar", "transportar"
- "origen", "destino", "planta", "almacén"
- "oferta", "demanda", "capacidad"
- "costo de transporte"

**Problemas de Asignación:**
- "asignar", "trabajador", "tarea"
- "matriz de costos", "emparejamiento"
- "eficiencia", "tiempo de ejecución"

**Teoría de Colas:**
- "cola", "espera", "fila"
- "servidor", "cliente", "llegadas"
- "tasa de servicio", "tiempo de espera"

### 3. Identificación de Elementos

#### Para Programación Lineal:
1. **Variables:** ¿Qué cantidades necesito determinar?
2. **Función Objetivo:** ¿Qué quiero maximizar o minimizar?
3. **Restricciones:** ¿Qué limitaciones tengo?
4. **Parámetros:** Coeficientes numéricos del problema

#### Para Transporte:
1. **Orígenes:** Puntos de suministro
2. **Destinos:** Puntos de demanda
3. **Ofertas:** Capacidad de cada origen
4. **Demandas:** Requerimientos de cada destino
5. **Costos:** Costo unitario de transporte

#### Para Colas:
1. **Patrón de llegadas:** ¿Cómo llegan los clientes?
2. **Patrón de servicio:** ¿Cómo se atienden?
3. **Número de servidores:** ¿Cuántos puntos de servicio?
4. **Capacidad:** ¿Hay límite en el sistema?

### 4. Formulación del Modelo

#### Pasos Generales:
1. **Definir variables** con notación clara
2. **Escribir la función objetivo** matemáticamente
3. **Listar todas las restricciones**
4. **Verificar** que el modelo sea completo y correcto

### 5. Selección del Método de Solución

#### Criterios de Selección:
- **Tamaño del problema:** Número de variables y restricciones
- **Tipo de variables:** Continuas, enteras, binarias
- **Estructura especial:** Transporte, asignación, etc.
- **Herramientas disponibles:** Manual vs. software

### 6. Interpretación de Resultados

#### Verificaciones Importantes:
1. **Factibilidad:** ¿La solución cumple todas las restricciones?
2. **Optimalidad:** ¿Es realmente la mejor solución?
3. **Sentido práctico:** ¿Los resultados son lógicos?
4. **Análisis de sensibilidad:** ¿Qué pasa si cambian los parámetros?

## Lista de Verificación para Análisis

### Antes de Resolver:
- [ ] Entiendo completamente el problema
- [ ] He identificado el tipo de problema correctamente
- [ ] He definido todas las variables necesarias
- [ ] He formulado el modelo matemático completo
- [ ] He seleccionado el método de solución apropiado

### Durante la Solución:
- [ ] Estoy siguiendo el método correctamente
- [ ] Los cálculos son precisos
- [ ] Estoy documentando cada paso
- [ ] Verifico restricciones en cada iteración

### Después de Resolver:
- [ ] La solución es factible
- [ ] He verificado la optimalidad
- [ ] Los resultados tienen sentido práctico
- [ ] He interpretado correctamente los resultados
- [ ] He considerado análisis de sensibilidad si es necesario

## Errores Comunes a Evitar

1. **No leer el problema completamente** antes de empezar
2. **Confundir el tipo de problema**
3. **Definir variables incorrectamente**
4. **Omitir restricciones importantes**
5. **Errores aritméticos en los cálculos**
6. **No verificar la factibilidad de la solución**
7. **Interpretar incorrectamente los resultados**
8. **No considerar el contexto práctico del problema**