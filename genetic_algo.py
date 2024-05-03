import random
import data_handler, formulas
from nltk.corpus import reuters

def init_population(population_size):
    keyboard_characters = "qwfpbjluyarstgkneio'zxcdvmh,.____"
    population = []
    for _ in range(population_size):
        population.append("".join(random.sample(keyboard_characters, len(keyboard_characters))))
        
    return population
    
def next_generation(population, data, mutation_rate):
    # Score each individual in the population using the fitness function
    population_score = {}
    for individual in population:
        population_score[individual] = formulas.fitness(individual, data)
        
    # Sort the population by their score
    population = sorted(population, key=lambda x: population_score[x], reverse=True)
    
    best_individual = population[0]
        
    # Create the next generation
    top_population = []
    new_population = []
        
    # Also add the top x percent to the new population without any changes
    elite_percent = 0.1
    for i in range(int(len(population) * elite_percent)):
        new_population.append(population[i])
        #new_population.append(mutate(population[i], mutation_rate))
        
    # Pick out pairs of three randomly from the population until all have been selected
    for _ in range(int(len(population) * (1 - elite_percent)) // 2):
        # Pick out three and delete them from the population
        choices = random.sample(population, 3)
            
        # Select best one from the three
        best_choice = max(choices, key=lambda x: population_score[x])
        top_population.append(best_choice)
        
    for _ in range(len(top_population)):
        parent1 = random.choice(top_population)
        parent2 = random.choice(top_population)
        child1, child2 = crossover(parent1, parent2)
        new_population.append(mutate(child1, mutation_rate))
        new_population.append(mutate(child2, mutation_rate))
        
    return new_population, best_individual

def crossover(parent1, parent2):
    from utils import convert_placeholder, revert_placeholder
    
    length = len(parent1)
    # Ensure parents are of equal length and not too short
    assert length == len(parent2) and length > 2, "Parents must be of equal and sufficient length"
    
    parent1 = convert_placeholder(parent1, '_')
    parent2 = convert_placeholder(parent2, '_')
    
    # Generate two crossover points
    cross_points = sorted(random.sample(range(1, length), 2))
    
    # Initialize children with placeholders
    child1 = [''] * length
    child2 = [''] * length
    
    # Swap substrings between parents based on crossover points
    child1[cross_points[0]:cross_points[1]] = parent2[cross_points[0]:cross_points[1]]
    child2[cross_points[0]:cross_points[1]] = parent1[cross_points[0]:cross_points[1]]
    
    # Mapping from parent to child for each crossover segment
    for i in range(cross_points[0], cross_points[1]):
        # Fill in the rest of child1
        if parent1[i] not in child1:
            j = i
            while child1[j] != '':
                j = parent1.index(parent2[j])
            child1[j] = parent1[i]
        # Fill in the rest of child2
        if parent2[i] not in child2:
            j = i
            while child2[j] != '':
                j = parent2.index(parent1[j])
            child2[j] = parent2[i]
    
    # Fill in remaining characters
    for i in range(length):
        if child1[i] == '':
            child1[i] = parent1[i]
        if child2[i] == '':
            child2[i] = parent2[i]
            
    child1 = revert_placeholder(''.join(child1), '_')
    child2 = revert_placeholder(''.join(child2), '_')
    
    return child1, child2

def mutate(s, n_percent):
    # Convert the string to a list of characters for easy manipulation
    chars = list(s)
    length = len(chars)
    
    for i in range(length):
        # Check if the current character should be mutated
        if random.randint(1, 100) <= n_percent:
            # Select a random index to swap with
            swap_index = random.randint(0, length - 1)
            # Swap the current character with the character at the swap_index
            chars[i], chars[swap_index] = chars[swap_index], chars[i]
    
    # Convert the list of characters back to a string
    return ''.join(chars)
    
# Selection
# Mutation / Crossover
# Repeat until stopping condition is met

def main():
    
    print("Genetic Algorithm... Running...")
    data = [data_handler.relative_letter_frequency(reuters, 'reuters'), data_handler.relative_bigram_frequency(reuters, 'reuters')]
    mutation_rate = 1
    
    top_individuals = []
    
    
    for _ in range(20):
        population = init_population(20)
        for i in range(200):
            population, best_individual = next_generation(population, data, mutation_rate)
            score = formulas.fitness(best_individual, data)
            print(f"====== Generation {i + 1}: {best_individual} - Score: {score} ======")
        top_individuals.append(best_individual)
        print(f"Top individual: {best_individual}")
        
    print("Top individuals:")
    for individual in top_individuals:
        print(individual)
        
    population = top_individuals
    for i in range(500):
        population, best_individual = next_generation(population, data, mutation_rate)
        score = formulas.fitness(best_individual, data)
        print(f"====== Generation {i + 1}: {best_individual} - Score: {score} ======")
        

main()

# Results: test_runs.py
    
    