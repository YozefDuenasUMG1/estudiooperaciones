#!/usr/bin/env python3
"""
Interactive Operations Research Problem Solver
Allows users to input and solve their own transportation and assignment problems
"""

from operations_research_solver import TransportationProblem, AssignmentProblem
import pandas as pd

def get_matrix_input(rows: int, cols: int, description: str) -> list:
    """Get matrix input from user"""
    print(f"\nEnter {description} ({rows}x{cols} matrix):")
    matrix = []
    for i in range(rows):
        while True:
            try:
                row_input = input(f"Row {i+1} (space-separated values): ")
                row = [float(x) for x in row_input.split()]
                if len(row) != cols:
                    print(f"Error: Please enter exactly {cols} values")
                    continue
                matrix.append(row)
                break
            except ValueError:
                print("Error: Please enter numeric values only")
    return matrix

def get_vector_input(size: int, description: str) -> list:
    """Get vector input from user"""
    while True:
        try:
            vector_input = input(f"Enter {description} (space-separated values): ")
            vector = [float(x) for x in vector_input.split()]
            if len(vector) != size:
                print(f"Error: Please enter exactly {size} values")
                continue
            return vector
        except ValueError:
            print("Error: Please enter numeric values only")

def solve_transportation_problem():
    """Interactive transportation problem solver"""
    print("\n" + "="*60)
    print("TRANSPORTATION PROBLEM SOLVER")
    print("="*60)
    
    # Get problem dimensions
    while True:
        try:
            m = int(input("Number of suppliers: "))
            n = int(input("Number of destinations: "))
            if m > 0 and n > 0:
                break
            print("Error: Number of suppliers and destinations must be positive")
        except ValueError:
            print("Error: Please enter integer values")
    
    # Get cost matrix
    costs = get_matrix_input(m, n, "cost matrix")
    
    # Get supply and demand
    supply = get_vector_input(m, "supply values")
    demand = get_vector_input(n, "demand values")
    
    # Display problem
    print(f"\nPROBLEM SUMMARY:")
    print(f"Cost Matrix:")
    print(pd.DataFrame(costs, 
                      index=[f"S{i+1}" for i in range(m)],
                      columns=[f"D{j+1}" for j in range(n)]))
    print(f"Supply: {supply}")
    print(f"Demand: {demand}")
    
    # Check balance
    total_supply = sum(supply)
    total_demand = sum(demand)
    print(f"Total Supply: {total_supply}")
    print(f"Total Demand: {total_demand}")
    
    if total_supply != total_demand:
        print("Warning: Problem is unbalanced. Will be balanced automatically.")
    
    # Solve problem
    tp = TransportationProblem(costs, supply, demand)
    
    print("\nChoose solution method:")
    print("1. Minimum Cost Method")
    print("2. Vogel's Approximation Method")
    print("3. Both methods")
    
    while True:
        try:
            choice = int(input("Enter choice (1-3): "))
            if choice in [1, 2, 3]:
                break
            print("Error: Please enter 1, 2, or 3")
        except ValueError:
            print("Error: Please enter a valid number")
    
    if choice == 1:
        tp.minimum_cost_method()
    elif choice == 2:
        tp.vogel_approximation_method()
    else:
        allocation1, cost1 = tp.minimum_cost_method()
        allocation2, cost2 = tp.vogel_approximation_method()
        print(f"\nCOMPARISON:")
        print(f"Minimum Cost Method Total Cost: {cost1}")
        print(f"Vogel's Method Total Cost: {cost2}")
        if cost1 < cost2:
            print("Minimum Cost Method gives better solution")
        elif cost2 < cost1:
            print("Vogel's Method gives better solution")
        else:
            print("Both methods give the same cost")

def solve_assignment_problem():
    """Interactive assignment problem solver"""
    print("\n" + "="*60)
    print("ASSIGNMENT PROBLEM SOLVER")
    print("="*60)
    
    # Get problem dimensions
    while True:
        try:
            n = int(input("Number of workers/tasks: "))
            if n > 0:
                break
            print("Error: Number must be positive")
        except ValueError:
            print("Error: Please enter integer values")
    
    # Get cost matrix
    costs = get_matrix_input(n, n, "cost matrix")
    
    # Display problem
    print(f"\nPROBLEM SUMMARY:")
    print(f"Cost Matrix:")
    print(pd.DataFrame(costs,
                      index=[f"Worker {i+1}" for i in range(n)],
                      columns=[f"Task {j+1}" for j in range(n)]))
    
    # Solve problem
    ap = AssignmentProblem(costs)
    assignments, total_cost = ap.hungarian_method()

def load_example_problems():
    """Load and solve example problems from the literature"""
    print("\n" + "="*60)
    print("EXAMPLE PROBLEMS")
    print("="*60)
    
    print("Available examples:")
    print("1. Transportation Problem Example")
    print("2. Assignment Problem Example")
    print("3. Unbalanced Transportation Problem")
    
    while True:
        try:
            choice = int(input("Choose example (1-3): "))
            if choice in [1, 2, 3]:
                break
            print("Error: Please enter 1, 2, or 3")
        except ValueError:
            print("Error: Please enter a valid number")
    
    if choice == 1:
        # Transportation problem example
        print("\nExample: Supply Chain Distribution Problem")
        costs = [
            [8, 6, 10, 9],
            [9, 12, 13, 7],
            [14, 9, 16, 5]
        ]
        supply = [20, 30, 25]
        demand = [15, 20, 15, 25]
        
        print("Three factories need to supply four warehouses:")
        print(pd.DataFrame(costs,
                          index=["Factory A", "Factory B", "Factory C"],
                          columns=["Warehouse 1", "Warehouse 2", "Warehouse 3", "Warehouse 4"]))
        print(f"Factory Capacity: {supply}")
        print(f"Warehouse Demand: {demand}")
        
        tp = TransportationProblem(costs, supply, demand)
        allocation1, cost1 = tp.minimum_cost_method()
        allocation2, cost2 = tp.vogel_approximation_method()
        
        print(f"\nSolution Comparison:")
        print(f"Minimum Cost Method: ${cost1}")
        print(f"Vogel's Method: ${cost2}")
        
    elif choice == 2:
        # Assignment problem example
        print("\nExample: Task Assignment Problem")
        costs = [
            [9, 2, 7, 8],
            [6, 4, 3, 7],
            [5, 8, 1, 8],
            [7, 6, 9, 4]
        ]
        
        print("Four workers need to be assigned to four tasks:")
        print(pd.DataFrame(costs,
                          index=["Worker A", "Worker B", "Worker C", "Worker D"],
                          columns=["Task 1", "Task 2", "Task 3", "Task 4"]))
        
        ap = AssignmentProblem(costs)
        assignments, total_cost = ap.hungarian_method()
        
    elif choice == 3:
        # Unbalanced transportation problem
        print("\nExample: Unbalanced Supply-Demand Problem")
        costs = [
            [2, 3, 11, 7],
            [1, 0, 6, 1],
            [5, 8, 15, 9]
        ]
        supply = [6, 1, 10]  # Total = 17
        demand = [7, 5, 3, 2]  # Total = 17 (balanced)
        
        # Make it unbalanced
        demand[0] = 10  # Total demand now = 20
        
        print("Supply doesn't match demand - will be balanced automatically:")
        print(pd.DataFrame(costs,
                          index=["Supplier 1", "Supplier 2", "Supplier 3"],
                          columns=["Customer A", "Customer B", "Customer C", "Customer D"]))
        print(f"Supply: {supply} (Total: {sum(supply)})")
        print(f"Demand: {demand} (Total: {sum(demand)})")
        
        tp = TransportationProblem(costs, supply, demand)
        allocation, cost = tp.vogel_approximation_method()

def main():
    """Main interactive interface"""
    print("OPERATIONS RESEARCH INTERACTIVE SOLVER")
    print("=" * 60)
    print("This tool solves Transportation and Assignment problems using:")
    print("• Minimum Cost Method")
    print("• Vogel's Approximation Method (VAM)")
    print("• Hungarian Method")
    print("=" * 60)
    
    while True:
        print("\nMain Menu:")
        print("1. Solve Transportation Problem")
        print("2. Solve Assignment Problem")
        print("3. View Example Problems")
        print("4. Exit")
        
        try:
            choice = int(input("Enter your choice (1-4): "))
            
            if choice == 1:
                solve_transportation_problem()
            elif choice == 2:
                solve_assignment_problem()
            elif choice == 3:
                load_example_problems()
            elif choice == 4:
                print("Thank you for using the Operations Research Solver!")
                break
            else:
                print("Error: Please enter a number between 1 and 4")
                
        except ValueError:
            print("Error: Please enter a valid number")
        except KeyboardInterrupt:
            print("\nGoodbye!")
            break
        
        # Ask if user wants to continue
        if choice in [1, 2, 3]:
            input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()