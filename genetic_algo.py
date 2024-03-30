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

# Score each individual in the population using the fitness function
population_score = []
for individual in population:
    population_score.append(formulas.fitness(individual, data))
    
# Selection
# Mutation / Crossover
# Repeat until stopping condition is met
