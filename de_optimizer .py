import numpy as np

def run_de(data, pop_size=30, generations=50, F=0.5, CR=0.7):
    n_items = len(data['values'])
    # Initialize Population (0 to 1)
    pop = np.random.rand(pop_size, n_items)
    history = []

    for gen in range(generations):
        new_pop = []
        for i in range(pop_size):
            # Mutation
            idxs = [idx for idx in range(pop_size) if idx != i]
            a, b, c = pop[np.random.choice(idxs, 3, replace=False)]
            mutant = np.clip(a + F * (b - c), 0, 1)
            
            # Crossover
            cross_points = np.random.rand(n_items) < CR
            trial = np.where(cross_points, mutant, pop[i])
            
            # Binary Mapping (If > 0.5, item is selected)
            binary_sol = (trial > 0.5).astype(int)
            
            # Repair Function (Check w1 Constraint)
            total_w1 = np.sum(binary_sol * data['w1'])
            if total_w1 > data['capacity']:
                # Simple repair: turn off items until it fits
                on_idxs = np.where(binary_sol == 1)[0]
                for idx in on_idxs:
                    binary_sol[idx] = 0
                    total_w1 -= data['w1'][idx]
                    if total_w1 <= data['capacity']: break
            
            new_pop.append(trial)
            
        pop = np.array(new_pop)
        # Track the best profit for the graph
        current_best = np.max([np.sum(((p > 0.5).astype(int)) * data['values']) for p in pop])
        history.append(current_best)

    return history, pop
