#!/usr/bin/env python3
"""
Operations Research Problem Solver
Solves transportation and assignment problems using various methods:
- Minimum Cost Method
- Vogel's Approximation Method (VAM)
- Hungarian Method for Assignment Problems
"""

import numpy as np
import pandas as pd
from typing import List, Tuple, Dict, Optional
import copy

class TransportationProblem:
    """Solver for Transportation Problems using Minimum Cost and Vogel's methods"""
    
    def __init__(self, costs: List[List[float]], supply: List[float], demand: List[float]):
        """
        Initialize transportation problem
        
        Args:
            costs: Cost matrix (suppliers x destinations)
            supply: Supply capacity for each supplier
            demand: Demand requirement for each destination
        """
        self.costs = np.array(costs, dtype=float)
        self.supply = np.array(supply, dtype=float)
        self.demand = np.array(demand, dtype=float)
        self.m, self.n = self.costs.shape  # m suppliers, n destinations
        
        # Check if problem is balanced
        if sum(self.supply) != sum(self.demand):
            self._balance_problem()
    
    def _balance_problem(self):
        """Balance the transportation problem by adding dummy supplier or destination"""
        total_supply = sum(self.supply)
        total_demand = sum(self.demand)
        
        if total_supply > total_demand:
            # Add dummy destination
            dummy_demand = total_supply - total_demand
            self.demand = np.append(self.demand, dummy_demand)
            dummy_costs = np.zeros((self.m, 1))
            self.costs = np.column_stack((self.costs, dummy_costs))
            self.n += 1
            print(f"Added dummy destination with demand {dummy_demand}")
            
        elif total_demand > total_supply:
            # Add dummy supplier
            dummy_supply = total_demand - total_supply
            self.supply = np.append(self.supply, dummy_supply)
            dummy_costs = np.zeros((1, self.n))
            self.costs = np.vstack((self.costs, dummy_costs))
            self.m += 1
            print(f"Added dummy supplier with supply {dummy_supply}")
    
    def minimum_cost_method(self) -> Tuple[np.ndarray, float]:
        """
        Solve using Minimum Cost Method
        
        Returns:
            allocation: Allocation matrix
            total_cost: Total transportation cost
        """
        print("\n=== MINIMUM COST METHOD ===")
        
        # Create working matrices
        supply_remaining = self.supply.copy()
        demand_remaining = self.demand.copy()
        allocation = np.zeros((self.m, self.n))
        
        # Create a list of all cells with their costs
        cells = []
        for i in range(self.m):
            for j in range(self.n):
                cells.append((self.costs[i, j], i, j))
        
        # Sort cells by cost (ascending)
        cells.sort()
        
        step = 1
        for cost, i, j in cells:
            if supply_remaining[i] > 0 and demand_remaining[j] > 0:
                # Allocate minimum of supply and demand
                allocation_amount = min(supply_remaining[i], demand_remaining[j])
                allocation[i, j] = allocation_amount
                supply_remaining[i] -= allocation_amount
                demand_remaining[j] -= allocation_amount
                
                print(f"Step {step}: Allocate {allocation_amount} to cell ({i+1},{j+1}) with cost {cost}")
                step += 1
                
                # If all supply or demand is satisfied, we can stop
                if sum(supply_remaining) == 0 or sum(demand_remaining) == 0:
                    break
        
        total_cost = np.sum(allocation * self.costs)
        
        print(f"\nAllocation Matrix:")
        print(pd.DataFrame(allocation, 
                         index=[f"S{i+1}" for i in range(self.m)],
                         columns=[f"D{j+1}" for j in range(self.n)]))
        print(f"Total Cost: {total_cost}")
        
        return allocation, total_cost
    
    def vogel_approximation_method(self) -> Tuple[np.ndarray, float]:
        """
        Solve using Vogel's Approximation Method (VAM)
        
        Returns:
            allocation: Allocation matrix
            total_cost: Total transportation cost
        """
        print("\n=== VOGEL'S APPROXIMATION METHOD ===")
        
        # Create working matrices
        supply_remaining = self.supply.copy()
        demand_remaining = self.demand.copy()
        allocation = np.zeros((self.m, self.n))
        costs_working = self.costs.copy()
        
        step = 1
        
        while np.sum(supply_remaining) > 0 and np.sum(demand_remaining) > 0:
            print(f"\nStep {step}:")
            
            # Calculate penalties for rows (suppliers)
            row_penalties = []
            for i in range(self.m):
                if supply_remaining[i] > 0:
                    available_costs = []
                    for j in range(self.n):
                        if demand_remaining[j] > 0:
                            available_costs.append(costs_working[i, j])
                    if len(available_costs) >= 2:
                        available_costs.sort()
                        penalty = available_costs[1] - available_costs[0]
                    elif len(available_costs) == 1:
                        penalty = available_costs[0]
                    else:
                        penalty = 0
                    row_penalties.append(penalty)
                else:
                    row_penalties.append(-1)  # Invalid row
            
            # Calculate penalties for columns (destinations)
            col_penalties = []
            for j in range(self.n):
                if demand_remaining[j] > 0:
                    available_costs = []
                    for i in range(self.m):
                        if supply_remaining[i] > 0:
                            available_costs.append(costs_working[i, j])
                    if len(available_costs) >= 2:
                        available_costs.sort()
                        penalty = available_costs[1] - available_costs[0]
                    elif len(available_costs) == 1:
                        penalty = available_costs[0]
                    else:
                        penalty = 0
                    col_penalties.append(penalty)
                else:
                    col_penalties.append(-1)  # Invalid column
            
            # Find maximum penalty
            max_row_penalty = max([p for p in row_penalties if p >= 0], default=0)
            max_col_penalty = max([p for p in col_penalties if p >= 0], default=0)
            
            if max_row_penalty >= max_col_penalty:
                # Choose row with maximum penalty
                selected_row = row_penalties.index(max_row_penalty)
                # Find minimum cost in selected row
                min_cost = float('inf')
                selected_col = -1
                for j in range(self.n):
                    if demand_remaining[j] > 0 and costs_working[selected_row, j] < min_cost:
                        min_cost = costs_working[selected_row, j]
                        selected_col = j
            else:
                # Choose column with maximum penalty
                selected_col = col_penalties.index(max_col_penalty)
                # Find minimum cost in selected column
                min_cost = float('inf')
                selected_row = -1
                for i in range(self.m):
                    if supply_remaining[i] > 0 and costs_working[i, selected_col] < min_cost:
                        min_cost = costs_working[i, selected_col]
                        selected_row = i
            
            # Allocate
            allocation_amount = min(supply_remaining[selected_row], demand_remaining[selected_col])
            allocation[selected_row, selected_col] = allocation_amount
            supply_remaining[selected_row] -= allocation_amount
            demand_remaining[selected_col] -= allocation_amount
            
            print(f"Row penalties: {[f'{p:.1f}' if p >= 0 else 'X' for p in row_penalties]}")
            print(f"Col penalties: {[f'{p:.1f}' if p >= 0 else 'X' for p in col_penalties]}")
            print(f"Allocate {allocation_amount} to cell ({selected_row+1},{selected_col+1}) with cost {min_cost}")
            
            # Remove exhausted supply or demand
            if supply_remaining[selected_row] == 0:
                print(f"Supplier {selected_row+1} exhausted")
            if demand_remaining[selected_col] == 0:
                print(f"Destination {selected_col+1} satisfied")
            
            step += 1
        
        total_cost = np.sum(allocation * self.costs)
        
        print(f"\nFinal Allocation Matrix:")
        print(pd.DataFrame(allocation, 
                         index=[f"S{i+1}" for i in range(self.m)],
                         columns=[f"D{j+1}" for j in range(self.n)]))
        print(f"Total Cost: {total_cost}")
        
        return allocation, total_cost

class AssignmentProblem:
    """Solver for Assignment Problems using Hungarian Method"""
    
    def __init__(self, costs: List[List[float]]):
        """
        Initialize assignment problem
        
        Args:
            costs: Cost matrix (workers x tasks)
        """
        self.original_costs = np.array(costs, dtype=float)
        self.n = len(costs)
        
        # Make matrix square if needed
        if len(costs) != len(costs[0]):
            max_size = max(len(costs), len(costs[0]))
            padded_costs = np.full((max_size, max_size), np.inf)
            for i in range(len(costs)):
                for j in range(len(costs[0])):
                    padded_costs[i, j] = costs[i][j]
            self.costs = padded_costs
            self.n = max_size
        else:
            self.costs = self.original_costs.copy()
    
    def hungarian_method(self) -> Tuple[List[Tuple[int, int]], float]:
        """
        Solve using Hungarian Method
        
        Returns:
            assignments: List of (worker, task) assignments
            total_cost: Total assignment cost
        """
        print("\n=== HUNGARIAN METHOD ===")
        
        # Step 1: Subtract row minima
        print("Step 1: Row reduction")
        cost_matrix = self.costs.copy()
        for i in range(self.n):
            row_min = np.min(cost_matrix[i, :])
            if row_min != np.inf:
                cost_matrix[i, :] -= row_min
                print(f"Row {i+1} minimum: {row_min}")
        
        print("After row reduction:")
        print(pd.DataFrame(cost_matrix))
        
        # Step 2: Subtract column minima
        print("\nStep 2: Column reduction")
        for j in range(self.n):
            col_min = np.min(cost_matrix[:, j])
            if col_min != np.inf and col_min > 0:
                cost_matrix[:, j] -= col_min
                print(f"Column {j+1} minimum: {col_min}")
        
        print("After column reduction:")
        print(pd.DataFrame(cost_matrix))
        
        # Step 3: Find minimum number of lines to cover all zeros with iteration limit
        iteration = 1
        max_iterations = 1000  # Prevent infinite loops
        
        while iteration <= max_iterations:
            print(f"\nIteration {iteration}:")
            
            # Find assignments using the current matrix
            assignments = self._find_optimal_assignment(cost_matrix)
            
            if len(assignments) == self.n:
                print("Optimal solution found!")
                break
            
            # Try to improve the solution
            cost_matrix = self._improve_hungarian_matrix(cost_matrix)
            print("Matrix improved for next iteration")
            
            iteration += 1
            
            if iteration > max_iterations:
                print(f"Warning: Reached maximum iterations ({max_iterations})")
                print("Using best assignment found so far")
                break
        
        # Calculate total cost using original cost matrix
        total_cost = 0
        valid_assignments = []
        
        for worker, task in assignments:
            if (worker < len(self.original_costs) and 
                task < len(self.original_costs[0]) and
                self.original_costs[worker, task] != np.inf):
                total_cost += self.original_costs[worker, task]
                valid_assignments.append((worker, task))
        
        print(f"\nOptimal Assignments:")
        for worker, task in valid_assignments:
            print(f"Worker {worker+1} -> Task {task+1} (Cost: {self.original_costs[worker, task]})")
        print(f"Total Cost: {total_cost}")
        
        return valid_assignments, total_cost
    
    def _find_optimal_assignment(self, matrix: np.ndarray) -> List[Tuple[int, int]]:
        """Find optimal assignment using greedy approach on zero elements"""
        assignments = []
        used_rows = set()
        used_cols = set()
        
        # First, try to find assignments where there's only one zero in row or column
        changed = True
        while changed:
            changed = False
            
            # Check for rows with only one zero
            for i in range(self.n):
                if i in used_rows:
                    continue
                zero_cols = [j for j in range(self.n) if j not in used_cols and matrix[i, j] == 0]
                if len(zero_cols) == 1:
                    j = zero_cols[0]
                    assignments.append((i, j))
                    used_rows.add(i)
                    used_cols.add(j)
                    changed = True
            
            # Check for columns with only one zero
            for j in range(self.n):
                if j in used_cols:
                    continue
                zero_rows = [i for i in range(self.n) if i not in used_rows and matrix[i, j] == 0]
                if len(zero_rows) == 1:
                    i = zero_rows[0]
                    assignments.append((i, j))
                    used_rows.add(i)
                    used_cols.add(j)
                    changed = True
        
        # For remaining assignments, use greedy approach
        while len(assignments) < self.n:
            best_assignment = None
            min_options = float('inf')
            
            for i in range(self.n):
                if i in used_rows:
                    continue
                for j in range(self.n):
                    if j in used_cols or matrix[i, j] != 0:
                        continue
                    
                    # Count options for this row and column
                    row_options = sum(1 for k in range(self.n) if k not in used_cols and matrix[i, k] == 0)
                    col_options = sum(1 for k in range(self.n) if k not in used_rows and matrix[k, j] == 0)
                    total_options = row_options + col_options
                    
                    if total_options < min_options:
                        min_options = total_options
                        best_assignment = (i, j)
            
            if best_assignment:
                i, j = best_assignment
                assignments.append((i, j))
                used_rows.add(i)
                used_cols.add(j)
            else:
                break
        
        return assignments
    
    def _improve_hungarian_matrix(self, matrix: np.ndarray) -> np.ndarray:
        """Improve the matrix by creating additional zeros"""
        # Find the minimum uncovered element
        assignments = self._find_optimal_assignment(matrix)
        used_rows = {row for row, col in assignments}
        used_cols = {col for row, col in assignments}
        
        # Find minimum element not covered by assignments
        min_uncovered = float('inf')
        for i in range(self.n):
            for j in range(self.n):
                if i not in used_rows or j not in used_cols:
                    if matrix[i, j] < min_uncovered:
                        min_uncovered = matrix[i, j]
        
        if min_uncovered == float('inf') or min_uncovered == 0:
            return matrix
        
        # Create new matrix by subtracting min_uncovered from uncovered elements
        # and adding it to doubly covered elements
        new_matrix = matrix.copy()
        for i in range(self.n):
            for j in range(self.n):
                if i not in used_rows and j not in used_cols:
                    # Uncovered element
                    new_matrix[i, j] -= min_uncovered
                elif i in used_rows and j in used_cols:
                    # Doubly covered element
                    new_matrix[i, j] += min_uncovered
        
        return new_matrix

def main():
    """Main function with example problems"""
    print("OPERATIONS RESEARCH PROBLEM SOLVER")
    print("=" * 50)
    
    # Example 1: Transportation Problem
    print("\nEXAMPLE 1: TRANSPORTATION PROBLEM")
    print("-" * 40)
    
    # Cost matrix (3 suppliers, 4 destinations)
    costs = [
        [8, 6, 10, 9],
        [9, 12, 13, 7],
        [14, 9, 16, 5]
    ]
    supply = [20, 30, 25]  # Supply capacity
    demand = [15, 20, 15, 25]  # Demand requirements
    
    print("Cost Matrix:")
    print(pd.DataFrame(costs, 
                      index=[f"Supplier {i+1}" for i in range(3)],
                      columns=[f"Dest {j+1}" for j in range(4)]))
    print(f"Supply: {supply}")
    print(f"Demand: {demand}")
    
    tp = TransportationProblem(costs, supply, demand)
    
    # Solve using Minimum Cost Method
    allocation1, cost1 = tp.minimum_cost_method()
    
    # Solve using Vogel's Approximation Method
    allocation2, cost2 = tp.vogel_approximation_method()
    
    print(f"\nCOMPARISON:")
    print(f"Minimum Cost Method: {cost1}")
    print(f"Vogel's Method: {cost2}")
    
    # Example 2: Assignment Problem
    print("\n" + "=" * 50)
    print("EXAMPLE 2: ASSIGNMENT PROBLEM")
    print("-" * 40)
    
    # Cost matrix (4 workers, 4 tasks)
    assignment_costs = [
        [9, 2, 7, 8],
        [6, 4, 3, 7],
        [5, 8, 1, 8],
        [7, 6, 9, 4]
    ]
    
    print("Cost Matrix:")
    print(pd.DataFrame(assignment_costs,
                      index=[f"Worker {i+1}" for i in range(4)],
                      columns=[f"Task {j+1}" for j in range(4)]))
    
    ap = AssignmentProblem(assignment_costs)
    assignments, total_cost = ap.hungarian_method()

if __name__ == "__main__":
    main()