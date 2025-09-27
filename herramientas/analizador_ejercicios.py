#!/usr/bin/env python3
"""
Analizador de Ejercicios de Investigación de Operaciones
Herramienta para identificar el tipo de problema y sugerir métodos de solución
"""

import re
import os
from typing import Dict, List, Tuple

class AnalizadorEjercicios:
    def __init__(self):
        self.tipos_problema = {
            'programacion_lineal': [
                'maximizar', 'minimizar', 'función objetivo', 'restricciones',
                'variables de decisión', 'simplex', 'programación lineal'
            ],
            'transporte': [
                'transporte', 'distribución', 'origen', 'destino', 'oferta',
                'demanda', 'costo de transporte', 'asignación de recursos'
            ],
            'asignacion': [
                'asignación', 'húngaro', 'trabajador', 'tarea', 'costo mínimo',
                'emparejamiento', 'matriz de costos'
            ],
            'teoria_colas': [
                'cola', 'espera', 'servidor', 'cliente', 'llegadas', 'servicio',
                'tasa de llegada', 'tasa de servicio', 'poisson'
            ],
            'inventarios': [
                'inventario', 'stock', 'demanda', 'costo de pedido',
                'costo de mantenimiento', 'EOQ', 'lote económico'
            ],
            'analisis_decisiones': [
                'decisión', 'árbol de decisión', 'incertidumbre',
                'alternativas', 'criterio', 'valor esperado'
            ]
        }
    
    def identificar_tipo_problema(self, texto: str) -> Dict[str, float]:
        """
        Identifica el tipo de problema basado en palabras clave
        Retorna un diccionario con los tipos y sus puntuaciones de confianza
        """
        texto_lower = texto.lower()
        puntuaciones = {}
        
        for tipo, palabras_clave in self.tipos_problema.items():
            puntuacion = 0
            for palabra in palabras_clave:
                if palabra in texto_lower:
                    puntuacion += 1
            
            # Normalizar por el número de palabras clave
            puntuaciones[tipo] = puntuacion / len(palabras_clave)
        
        return puntuaciones
    
    def sugerir_metodo_solucion(self, tipo_problema: str) -> List[str]:
        """
        Sugiere métodos de solución basados en el tipo de problema
        """
        metodos = {
            'programacion_lineal': [
                'Método Gráfico (si son 2 variables)',
                'Método Simplex',
                'Análisis de sensibilidad',
                'Software: PuLP, Gurobi, CPLEX'
            ],
            'transporte': [
                'Método de la Esquina Noroeste',
                'Método del Costo Mínimo',
                'Método de Vogel (VAM)',
                'Optimización con MODI'
            ],
            'asignacion': [
                'Método Húngaro',
                'Formulación como problema de transporte',
                'Algoritmos de emparejamiento'
            ],
            'teoria_colas': [
                'Identificar el modelo (M/M/1, M/M/s, etc.)',
                'Calcular medidas de desempeño',
                'Análisis de costos',
                'Simulación si es necesario'
            ],
            'inventarios': [
                'Modelo EOQ básico',
                'Modelo con descuentos por cantidad',
                'Modelos estocásticos',
                'Análisis ABC'
            ],
            'analisis_decisiones': [
                'Construcción del árbol de decisión',
                'Criterio del valor esperado',
                'Análisis de sensibilidad',
                'Criterios bajo incertidumbre'
            ]
        }
        
        return metodos.get(tipo_problema, ['Problema no reconocido'])
    
    def analizar_ejercicio(self, texto_ejercicio: str) -> Dict:
        """
        Análisis completo de un ejercicio
        """
        puntuaciones = self.identificar_tipo_problema(texto_ejercicio)
        tipo_principal = max(puntuaciones, key=puntuaciones.get)
        confianza = puntuaciones[tipo_principal]
        
        metodos = self.sugerir_metodo_solucion(tipo_principal)
        
        return {
            'tipo_problema': tipo_principal,
            'confianza': confianza,
            'todas_puntuaciones': puntuaciones,
            'metodos_sugeridos': metodos,
            'plantilla_recomendada': f'plantillas/{tipo_principal}.md'
        }
    
    def generar_reporte_analisis(self, ejercicio: str, archivo_salida: str = None):
        """
        Genera un reporte completo del análisis
        """
        analisis = self.analizar_ejercicio(ejercicio)
        
        reporte = f"""
# Análisis del Ejercicio

## Ejercicio Original
{ejercicio}

## Tipo de Problema Identificado
**Tipo Principal:** {analisis['tipo_problema'].replace('_', ' ').title()}
**Nivel de Confianza:** {analisis['confianza']:.2%}

## Puntuaciones por Tipo
"""
        for tipo, puntuacion in sorted(analisis['todas_puntuaciones'].items(), 
                                     key=lambda x: x[1], reverse=True):
            reporte += f"- {tipo.replace('_', ' ').title()}: {puntuacion:.2%}\n"
        
        reporte += f"""
## Métodos de Solución Recomendados
"""
        for i, metodo in enumerate(analisis['metodos_sugeridos'], 1):
            reporte += f"{i}. {metodo}\n"
        
        reporte += f"""
## Plantilla Recomendada
Utilizar: `{analisis['plantilla_recomendada']}`

## Próximos Pasos
1. Revisar la plantilla recomendada
2. Identificar las variables y parámetros específicos
3. Formular el modelo matemático
4. Aplicar el método de solución más apropiado
5. Interpretar y validar los resultados
"""
        
        if archivo_salida:
            with open(archivo_salida, 'w', encoding='utf-8') as f:
                f.write(reporte)
            print(f"Reporte guardado en: {archivo_salida}")
        
        return reporte

if __name__ == "__main__":
    # Ejemplo de uso
    analizador = AnalizadorEjercicios()
    
    ejercicio_ejemplo = """
    Una empresa produce dos tipos de productos A y B. 
    El producto A requiere 2 horas de máquina y 1 hora de mano de obra,
    generando una ganancia de $30. El producto B requiere 1 hora de máquina
    y 2 horas de mano de obra, con ganancia de $20.
    La empresa dispone de 100 horas de máquina y 80 horas de mano de obra.
    ¿Cuántos productos de cada tipo debe producir para maximizar la ganancia?
    """
    
    print("=== ANALIZADOR DE EJERCICIOS DE INVESTIGACIÓN DE OPERACIONES ===")
    print(analizador.generar_reporte_analisis(ejercicio_ejemplo))