# Formulas depending on letter frequency:
# Workload distribution
from workload_dist import get_combination_workload_dist_at, get_workload_dist_at
from utils import convert_to_layout, get_position_of_char, get_position_of_bigram

layout = { '11': 'q', '12': 'w', '13': 'e', '14': 'r', '15': 't', '16': 'y', '17': 'u', '18': 'i', '19': 'o', '20': 'p', '21': 'a', '22': 's', '23': 'd', '24': 'f', '25': 'g', '26': 'h', '27': 'j', '28': 'k', '29': 'l', '30': 'z', '31': 'x', '32': 'c', '33': 'v', '34': 'b', '35': 'n', '36': 'm' }

def workload_distribution_score(layout, data):
    # Calculate the workload distribution score of the layout
    
    layout = convert_to_layout(layout)
    
    score = 0
    for (letter, freq) in data.items():
        #print("====================================")
        #print(f"Letter: {letter}")
        #print(f"Freq: {freq}")
        #print(f"Position: {get_position_of_char(layout, letter)}")
        #print(f"Workload Dist: {get_workload_dist_at(get_position_of_char(layout, letter))}")
        #print(f"Freq - Workload Dist: {freq - get_workload_dist_at(get_position_of_char(layout, letter))}")
        #print(f"Square: {(freq - get_workload_dist_at(get_position_of_char(layout, letter)))**2}")
        #print("====================================")
        freq = freq * 100
        score += (freq + get_workload_dist_at(get_position_of_char(layout, letter)))**2
    
    return score

# Formulas depending on bigram frequency:
# Combination workload distribution
def combination_workload_distribution_score(layout, data):
    # Calculate the combination workload distribution score of the layout
    layout = convert_to_layout(layout)
    
    score = 0
    for (bigram, freq) in data.items():
        freq = freq * 100
        score += (freq + get_combination_workload_dist_at(get_position_of_bigram(layout, bigram)))**2
    
    return score

def fitness(layout, data):
    # Calculate the fitness of the layout
    x, y = 10, 1
    single_score = workload_distribution_score(layout, data[0])
    combination_score = combination_workload_distribution_score(layout, data[1])
    
    #print(f"Single Score: {single_score}")
    #print(f"Combination Score: {combination_score}")
    
    score = x * single_score + y * combination_score
    
    return score