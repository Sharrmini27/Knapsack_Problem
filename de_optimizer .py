import numpy as np

def repair_solution(solution, w1, capacity):
    """If weight exceeds capacity, remove items with worst value/weight ratio"""
    # implementation of the repair function
    return repaired_solution

def run_de(instance_data, pop_size=50, generations=100, F=0.8, CR=0.7):
    # 1. Initialize Population (random floats 0.0 to 1.0)
    # 2. Loop Generations:
    #    a. Mutation: V = X1 + F * (X2 - X3)
    #    b. Crossover: Mix mutant with target
    #    c. Selection: Evaluate Fitness (Profit) vs (W2 usage)
    # 3. Maintain Pareto Front (Non-dominated solutions)
    return pareto_front, history
