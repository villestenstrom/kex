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

def convert_to_layout(layout_string):
    layout = {}
    # Layout string is a string of characters representing the keyboard layout
    # The first 11 characters are the top row (11 - 111), the next 11 are the second row (21 - 211), the next 11 are the third row (31 - 311)
    # The format of the layout {} is {<key>: <character>}
    
    for i in range(3):
        for j in range(11):
            layout[str(i+1) + str(j+1)] = layout_string[i*11 + j]
            
    return layout

def show_layout(layout):
    print("==============LAYOUT==============")
    for i in range(3):
        if i == 0:
            print(' ', end='')
        elif i == 1:
            print('  ', end='')
        for j in range(11):
            print(layout[str(i+1) + str(j+1)] + " ", end=' ')
        print()
    print("==================================")

def get_position_of_char(layout, char):
    for position, character in layout.items():
        if character == char:
            return position
    return None

def get_position_of_bigram(layout, bigram):
    first, second = bigram
    first_pos = get_position_of_char(layout, first)
    second_pos = get_position_of_char(layout, second)
    return first_pos, second_pos


        
    