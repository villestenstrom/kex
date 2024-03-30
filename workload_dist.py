home_top_offset = 0.25
home_bottom_offset = 0.5
top_bottom_offset = 0.25
home_row_placement = {
    '1': '21', '2': '22', '3': '23', '4': '24', '5': '27', '6': '28', '7': '29', '8': '210',
}
import math

def generate_workload_dist(keymap, penalty_map):
    # This function generates a value for each key in the keymap
    # This is determined by a set of criteria
    # We would base the workload on the following criteria (Easy to Determine):
    # 1. (FD) Finger dexterity (ETD)
    # 2. (TD) Travel distance (ETD)
    # 3. (FC) Finger comfort (shorter fingers would be more comfortable on the bottom row than the top row)
    # 4. (KC) Key count, the # of keys that are already handled by the finger
    
    # The formula for the workload distribution would be:
    # W = x * FD + y * TD + z * FC + w * KC, where x, y, z, and w are weights for each criteria
    # We set the weights to 1 for now
    x, y, z, w = 1, 1, 1, 1
    y = 1
    z = 1
    
    def calculate_travel_distance_from_home_row(keymap):
        travel_distance_map = {}
        for (key, value) in keymap:
            original_placement = home_row_placement[value]
            row_offset = int(key[0]) - int(original_placement[0])
            column_offset = abs(int(key[1:]) - int(original_placement[1:]))
            
            if row_offset == 0:
                distance = column_offset
            elif row_offset == -1:
                distance = math.sqrt((column_offset + home_top_offset) ** 2 + 1)
            else:
                distance = math.sqrt((column_offset + home_bottom_offset) ** 2 + 1)
            
            travel_distance_map[key] = distance
        return travel_distance_map
    
    def calculate_number_of_keys_handled_by_finger(keymap):
        key_count_map = {}
        for (key, value) in keymap:
            key_count = 0
            for (k, v) in keymap:
                if v == value:
                    key_count += 1
            key_count_map[value] = key_count
        return key_count_map
    
    workload_distribution_map = {}
    
    for (key, value) in keymap:
        W = x * penalty_map['finger_dexterity'][value] + y * (4 - calculate_travel_distance_from_home_row(keymap)[key]) + z * penalty_map['finger_comfort'][key] - w * (calculate_number_of_keys_handled_by_finger(keymap)[value] * penalty_map['penalty_per_key_handled'][value])
        W = round(W, 4)
        workload_distribution_map[key] = W
    
    return workload_distribution_map



def generate_combination_workload_dist(keymap, penalty_map):
    # This function generates a value for each key combination in the keymap
    # This is determined by a set of criteria
    # We would base the workload on the following criteria:
    # Penalities for:
    # Key transitions:
    # 1. Rollout (from thumb to pinky)
    # 2. Same finger twice for non-repeating characters
    # 3. Finger placements:
    # 3.1 P_one_over_R
    # 3.2 P_two_over_R
    # 3.2 R_one_over_M
    # 3.3 R_two_over_M
    # 3.4 I_one_over_M
    # 3.5 I_two_over_M
    # 4. At least one finger not on home row
    # 5. One finger on top row and one finger on bottom row
    # 6. Hand movement (reaching with index finger to b causes rest of fingers to move compared to reaching for y)
    
    # We need to define what each penalty means over the keymap
    # We store all penalties in a dictionary accessible by the penalty name
    # For example the key positions penalty would have the key be the key id and the value be the penalty value for that key
    
    for (key, value) in keymap:
        for penalty in penalty_map:
            pass
    
    pass

# Keymap would consist of the following:
# Dictionary of key-value pairs where the key is the id of the key and the value is the finger that presses the key
# The top left key (q) would be 11, and the top right key (p) would be 110
# The leftmost key on the second row (a) would be 21, and the rightmost key on the second row (ö) would be 210
# The bottom left key (<) would be 31, and the bottom right key (m) would be 310
# Fingers would be represented by numbers from 1 to 8, where 1 is the left pinky and 8 is the right pinky
keymap = {
     '11': '1', '12': '2', '13': '3', '14': '4', '15': '4', '16': '5', '17': '5', '18': '6', '19': '7', '110': '8', '111': '8',
       '21': '1', '22': '2', '23': '3', '24': '4', '25': '4', '26': '5', '27': '5', '28': '6', '29': '7', '210': '8', '211': '8', 
    '31': '1', '32': '2', '33': '3', '34': '4', '35': '4', '36': '4', '37': '5', '38': '5', '39': '6', '310': '7', '311': '8',
}


penalty_map_1 = {
    'finger_dexterity': {
        '1': 0.15, '2': 0.25, '3': 0.35, '4': 0.25, '5': 0.25, '6': 0.35, '7': 0.25, '8': 0.15
    },
    'finger_comfort': {
         '11': 0.2, '12': 0.9,  '13': 0.9, '14': 0.6, '15': 0.5, '16': 0.2, '17': 0.7, '18': 0.9, '19': 0.9, '110': 0.3, '111': 0.3,
           '21': 1, '22': 1, '23': 1, '24': 1, '25': 0.8, '26': 0.8, '27': 1, '28': 1, '29': 1, '210': 1, '211': 0.8,
        '31': 0.8, '32': 0.6, '33': 0.5, '34': 0.8, '35': 0.7, '36': 0.2, '37': 0.7, '38': 0.8, '39': 0.5, '310': 0.6, '311': 0.8,
    },
    'penalty_per_key_handled': {
        '1': 0.1, '2': 0.1, '3': 0.1, '4': 0.1, '5': 0.1, '6': 0.1, '7': 0.1, '8': 0.1
    }
}

penalty_map_2 = {
    'key_positions': {
        '11': 0, '12': 0, '13': 0, '14': 0, '15': 0, '16': 0, '17': 0, '18': 0, '19': 0, '110': 0, '111': 0,
        '21': 0, '22': 0, '23': 0, '24': 0, '25': 0, '26': 0, '27': 0, '28': 0, '29': 0, '210': 0, '211': 0,
        '31': 0, '32': 0, '33': 0, '34': 0, '35': 0, '36': 0, '37': 0, '38': 0, '39': 0, '310': 0, '311': 0,
    },
    'key_transitions': {
        '11': 0, '12': 0, '13': 0, '14': 0, '15': 0, '16': 0, '17': 0, '18': 0, '19': 0, '110': 0, '111': 0,
        '21': 0, '22': 0, '23': 0, '24': 0, '25': 0, '26': 0, '27': 0, '28': 0, '29': 0, '210': 0, '211': 0,
        '31': 0, '32': 0, '33': 0, '34': 0, '35': 0, '36': 0, '37': 0, '38': 0, '39': 0, '310': 0, '311': 0,
    }
}

# Run
workload_dist = generate_workload_dist(keymap.items(), penalty_map_1)

print(workload_dist)