import random
import data_handler, formulas
from nltk.corpus import reuters

def init_population(population_size):
    keyboard_characters = "qwfpbjluyarstgkneio'zxcdvmh,."
    population = []
    for _ in range(population_size):
        population.append("".join(random.sample(keyboard_characters, len(keyboard_characters))))
        
    return population

population = init_population(10)

data = [data_handler.relative_letter_frequency(reuters, 'reuters'), data_handler.relative_bigram_frequency(reuters, 'reuters')]

    
def next_generation(population):
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
    for _ in range(len(population)):
        parent1 = random.choice(top_population)
        parent2 = random.choice(top_population)
        new_population.append(crossover(parent1, parent2))
        
    # Also add the top x percent to the new population without any changes
    elite_percent = 0.1
    for i in range(int(len(population) * elite_percent)):
        new_population.append(population[i])
        
    return new_population

def crossover(layout1, layout2):
    pass
    
# Selection
# Mutation / Crossover
# Repeat until stopping condition is met
