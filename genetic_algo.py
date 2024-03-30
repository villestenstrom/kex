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
    population_score = []
    for individual in population:
        population_score.append(formulas.fitness(individual, data))
        
    # Sort the population by their score
    population = [x for _, x in sorted(zip(population_score, population), key=lambda pair: pair[0], reverse=True)]
        
    # Select the top x percent of the population for reproduction
    top_percent = 0.4
    top_population = []
    for i in range(int(len(population) * top_percent)):
        top_population.append(population[i])
        
    # Create the next generation
    new_population = []
    for _ in range(len(top_population)):
        parent1 = random.choice(top_population)
        parent2 = random.choice(top_population)
        child1, child2 = crossover(parent1, parent2)
        new_population.append(mutate(child1, mutation_rate))
        new_population.append(mutate(child2, mutation_rate))
        
    # Also add the top x percent to the new population without any changes
    elite_percent = 0.2
    for i in range(int(len(population) * elite_percent)):
        new_population.append(population[i])
        
    return new_population, population[0]

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

    population = init_population(100)
    data = [data_handler.relative_letter_frequency(reuters, 'reuters'), data_handler.relative_bigram_frequency(reuters, 'reuters')]
    mutation_rate = 10
    
    for i in range(1000):
        population, best_individual = next_generation(population, data, mutation_rate)
        print(len(population))
        score = formulas.fitness(best_individual, data)
        print(f"====== Generation {i + 1}: {best_individual} - Score: {score} ======")

main()

# Results: test_runs.py
    
    