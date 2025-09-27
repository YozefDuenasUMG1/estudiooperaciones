# Cómo Usar Este Repositorio

## Para Analizar un Ejercicio Nuevo

### Método 1: Análisis Automático
1. Ejecutar el analizador de ejercicios:
   ```bash
   cd herramientas
   python3 analizador_ejercicios.py
   ```
   
2. O analizar un ejercicio específico desde Python:
   ```python
   from herramientas.analizador_ejercicios import AnalizadorEjercicios
   
   analizador = AnalizadorEjercicios()
   texto_ejercicio = "Tu ejercicio aquí..."
   reporte = analizador.generar_reporte_analisis(texto_ejercicio)
   print(reporte)
   ```

### Método 2: Análisis Manual
1. **Leer la guía de análisis:** `documentos/guia_analisis.md`
2. **Identificar el tipo de problema** usando las palabras clave
3. **Seleccionar la plantilla apropiada** de la carpeta `plantillas/`
4. **Seguir la estructura** de la plantilla para resolver

## Estructura de Trabajo Recomendada

### Para un Ejercicio Nuevo:
1. **Crear el archivo del ejercicio** en `ejercicios/nombre_ejercicio.md`
2. **Usar el analizador** para identificar el tipo
3. **Copiar la plantilla apropiada** a `soluciones/solucion_nombre_ejercicio.md`
4. **Completar la solución** paso a paso
5. **Verificar los resultados**

### Ejemplo de Flujo de Trabajo:
```bash
# 1. Crear ejercicio
echo "Mi ejercicio..." > ejercicios/problema_produccion.md

# 2. Analizar tipo
python3 herramientas/analizador_ejercicios.py

# 3. Copiar plantilla
cp plantillas/programacion_lineal.md soluciones/solucion_problema_produccion.md

# 4. Editar y resolver
# (completar la plantilla con los datos específicos)
```

## Tipos de Problemas Soportados

1. **Programación Lineal** → `plantillas/programacion_lineal.md`
2. **Transporte** → `plantillas/transporte.md`
3. **Teoría de Colas** → `plantillas/teoria_colas.md`
4. Más plantillas se pueden agregar según necesidad

## Herramientas Disponibles

- **analizador_ejercicios.py**: Identifica automáticamente el tipo de problema
- **Plantillas**: Estructuras predefinidas para cada tipo de problema
- **Ejemplos**: Casos resueltos para referencia

## Consejos para Mejores Resultados

1. **Descripción clara**: Incluye todos los datos numéricos
2. **Contexto específico**: Menciona el tipo de industria o aplicación
3. **Pregunta precisa**: Define exactamente qué se necesita calcular
4. **Verificación**: Siempre verifica que la solución sea factible y lógica