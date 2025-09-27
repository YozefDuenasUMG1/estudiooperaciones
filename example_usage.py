#!/usr/bin/env python3
"""
Example Usage of Operations Research Solver
Demonstrates how to use the solver for different types of problems
"""

from operations_research_solver import TransportationProblem, AssignmentProblem
import pandas as pd

def example_1_balanced_transportation():
    """Example 1: Balanced Transportation Problem"""
    print("="*60)
    print("EJEMPLO 1: PROBLEMA DE TRANSPORTE BALANCEADO")
    print("="*60)
    
    print("Problema: Una empresa tiene 3 fábricas que deben abastecer 4 centros de distribución")
    
    # Matriz de costos de transporte por unidad
    costs = [
        [4, 2, 8, 6],   # Fábrica A
        [3, 7, 5, 1],   # Fábrica B  
        [6, 4, 3, 9]    # Fábrica C
    ]
    
    supply = [30, 50, 40]    # Capacidad de producción
    demand = [25, 35, 30, 30]  # Demanda de los centros
    
    print(f"Oferta total: {sum(supply)} unidades")
    print(f"Demanda total: {sum(demand)} unidades")
    print("✅ Problema balanceado\n")
    
    # Mostrar datos del problema
    df_costs = pd.DataFrame(costs, 
                           index=['Fábrica A', 'Fábrica B', 'Fábrica C'],
                           columns=['Centro 1', 'Centro 2', 'Centro 3', 'Centro 4'])
    print("Matriz de Costos de Transporte:")
    print(df_costs)
    print(f"\nCapacidad de producción: {supply}")
    print(f"Demanda de los centros: {demand}")
    
    # Resolver el problema
    tp = TransportationProblem(costs, supply, demand)
    
    print("\n" + "="*40)
    print("SOLUCIÓN USANDO MÉTODO DEL COSTO MÍNIMO")
    print("="*40)
    allocation1, cost1 = tp.minimum_cost_method()
    
    print("\n" + "="*40)
    print("SOLUCIÓN USANDO MÉTODO DE VOGEL")
    print("="*40)
    allocation2, cost2 = tp.vogel_approximation_method()
    
    print(f"\n📊 COMPARACIÓN DE MÉTODOS:")
    print(f"Método del Costo Mínimo: ${cost1:,.2f}")
    print(f"Método de Vogel: ${cost2:,.2f}")
    
    if cost1 < cost2:
        print("✅ El Método del Costo Mínimo es mejor")
    elif cost2 < cost1:
        print("✅ El Método de Vogel es mejor")
    else:
        print("✅ Ambos métodos producen el mismo costo")

def example_2_unbalanced_transportation():
    """Example 2: Unbalanced Transportation Problem"""
    print("\n" + "="*60)
    print("EJEMPLO 2: PROBLEMA DE TRANSPORTE NO BALANCEADO")
    print("="*60)
    
    print("Problema: Distribución de medicamentos con exceso de demanda")
    
    # Matriz de costos
    costs = [
        [5, 8, 6],     # Hospital A
        [4, 7, 9],     # Hospital B
        [6, 5, 4]      # Hospital C
    ]
    
    supply = [100, 150, 120]  # Disponibilidad de medicamentos
    demand = [80, 140, 200, 60]  # Demanda de hospitales (total = 480)
    
    print(f"Oferta total: {sum(supply)} unidades")
    print(f"Demanda total: {sum(demand)} unidades")
    print("⚠️ Problema no balanceado (demanda > oferta)")
    print("Se agregará un proveedor ficticio automáticamente\n")
    
    # Mostrar datos
    df_costs = pd.DataFrame(costs,
                           index=['Proveedor A', 'Proveedor B', 'Proveedor C'],
                           columns=['Hospital 1', 'Hospital 2', 'Hospital 3'])
    print("Matriz de Costos:")
    print(df_costs)
    print(f"\nDisponibilidad: {supply}")
    print(f"Demanda: {demand}")
    
    # Resolver
    tp = TransportationProblem(costs, supply, demand)
    allocation, cost = tp.vogel_approximation_method()
    
    print(f"\n💰 Costo total de distribución: ${cost:,.2f}")

def example_3_assignment_problem():
    """Example 3: Assignment Problem"""
    print("\n" + "="*60)
    print("EJEMPLO 3: PROBLEMA DE ASIGNACIÓN")
    print("="*60)
    
    print("Problema: Asignar 4 empleados a 4 proyectos para minimizar tiempo total")
    
    # Matriz de tiempos (en horas) - 4x4 para simplificar
    times = [
        [12, 8, 15, 10],   # Empleado A
        [9, 11, 7, 14],    # Empleado B
        [16, 5, 13, 8],    # Empleado C
        [7, 14, 11, 6]     # Empleado D
    ]
    
    # Mostrar datos
    df_times = pd.DataFrame(times,
                           index=['Empleado A', 'Empleado B', 'Empleado C', 'Empleado D'],
                           columns=['Proyecto 1', 'Proyecto 2', 'Proyecto 3', 'Proyecto 4'])
    print("Matriz de Tiempos de Ejecución (horas):")
    print(df_times)
    
    # Resolver usando método húngaro
    ap = AssignmentProblem(times)
    assignments, total_time = ap.hungarian_method()
    
    print(f"\n⏱️ Tiempo total mínimo: {total_time} horas")
    
    print("\n📋 ASIGNACIÓN ÓPTIMA DETALLADA:")
    for i, (worker, project) in enumerate(assignments, 1):
        worker_name = ['Empleado A', 'Empleado B', 'Empleado C', 'Empleado D'][worker]
        project_name = f'Proyecto {project + 1}'
        time = times[worker][project]
        print(f"{i}. {worker_name} → {project_name} ({time} horas)")

def example_4_real_world_scenario():
    """Example 4: Real-world delivery optimization"""
    print("\n" + "="*60)
    print("EJEMPLO 4: OPTIMIZACIÓN DE ENTREGAS REAL")
    print("="*60)
    
    print("Problema: Empresa de paquetería debe optimizar rutas de entrega")
    print("Centros de distribución → Zonas de entrega")
    
    # Costos de entrega por paquete (en $)
    delivery_costs = [
        [2.5, 3.0, 4.5, 2.8, 3.5],  # Centro Norte
        [3.2, 2.1, 3.8, 4.0, 2.9],  # Centro Sur
        [4.1, 3.6, 2.3, 3.1, 4.2],  # Centro Este
        [2.7, 4.3, 3.4, 2.6, 3.7]   # Centro Oeste
    ]
    
    supply = [500, 400, 350, 600]  # Capacidad de paquetes por día
    demand = [300, 280, 320, 450, 500]  # Demanda por zona
    
    print("Capacidad de centros (paquetes/día):", supply)
    print("Demanda por zona (paquetes/día):", demand)
    
    # Crear DataFrame para mejor visualización
    zones = ['Zona A', 'Zona B', 'Zona C', 'Zona D', 'Zona E']
    centers = ['Centro Norte', 'Centro Sur', 'Centro Este', 'Centro Oeste']
    
    df_costs = pd.DataFrame(delivery_costs, index=centers, columns=zones)
    print("\nCostos de Entrega por Paquete ($):")
    print(df_costs)
    
    # Resolver
    tp = TransportationProblem(delivery_costs, supply, demand)
    
    print("\n🚚 OPTIMIZACIÓN DE RUTAS:")
    allocation, cost = tp.vogel_approximation_method()
    
    print(f"\n💵 Costo total diario de entregas: ${cost:,.2f}")
    print(f"📊 Costo promedio por paquete: ${cost/sum(demand):.2f}")
    
    # Mostrar rutas recomendadas
    print("\n🗺️ RUTAS RECOMENDADAS:")
    for i in range(len(centers)):
        for j in range(len(zones)):
            if allocation[i, j] > 0:
                print(f"{centers[i]} → {zones[j]}: {int(allocation[i, j])} paquetes (${delivery_costs[i][j]:.2f} c/u)")

def main():
    """Run all examples"""
    print("🔬 EJEMPLOS DE INVESTIGACIÓN DE OPERACIONES")
    print("Implementación de algoritmos clásicos de optimización")
    print("="*60)
    
    try:
        example_1_balanced_transportation()
        example_2_unbalanced_transportation()
        example_3_assignment_problem()
        example_4_real_world_scenario()
        
        print("\n" + "="*60)
        print("✅ TODOS LOS EJEMPLOS COMPLETADOS EXITOSAMENTE")
        print("="*60)
        print("Para usar con tus propios datos:")
        print("• python interactive_solver.py  (interfaz interactiva)")
        print("• Modificar este archivo con tus datos específicos")
        print("• Importar las clases en tu propio código Python")
        
    except Exception as e:
        print(f"❌ Error durante la ejecución: {e}")
        raise

if __name__ == "__main__":
    main()