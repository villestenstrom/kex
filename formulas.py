# Formulas depending on letter frequency:
# Workload distribution
def workload_distribution_score(layout, data):
    # Calculate the workload distribution score of the layout
    
    return 0

# Formulas depending on bigram frequency:
# Combination workload distribution
def combination_workload_distribution_score(layout, data):
    # Calculate the combination workload distribution score of the layout
    
    return 0

def fitness(layout, data):
    # Calculate the fitness of the layout
    x, y = 1, 1
    
    score = x * workload_distribution_score(layout, data[0]) + y * combination_workload_distribution_score(layout, data[1])
    
    return x * workload_distribution_score(layout, data[0]) + y * combination_workload_distribution_score(layout, data[1])