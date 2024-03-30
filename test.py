import random

import random

def convert_placeholder(text, placeholder):
    count = 1
    while placeholder in text:
        text = text.replace(placeholder, str(count), 1)
        count += 1
    return text

def revert_placeholder(text, placeholder):
    for number in range(1, 10):
        text = text.replace(str(number), placeholder)
    return text

def pmx_crossover(parent1, parent2):
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

# Example parents
parent1 = "qwfpbj__luy_ars_tgkneio'zxcdvmh,."
parent2 = "a_rstgkneio'zx_cd_vmh,.qwfpbjluy_"

child1, child2 = pmx_crossover(parent1, parent2)

# Example parents

def mutate_string(s, n_percent):
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

# Example usage
mutation_rate = 1  # 10% chance of mutation per key
mutated_layout1 = mutate_string(child1, mutation_rate)
mutated_layout2 = mutate_string(child2, mutation_rate)
