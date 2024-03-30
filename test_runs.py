
from utils import convert_to_layout, show_layout
from formulas import fitness
import data_handler
from nltk.corpus import reuters

layout_string = 'dxfq__.csa_hgymobwplnekvjz\'_,uitr'
layout = convert_to_layout(layout_string)
show_layout(layout)

# ====== Generation 922: qxj__.,ac__gkdmshblpnevfzyt'wuior - Score: 10500.173068545553 ======
# dxfq__.csa_hgymobwplnekvjz'_,uitr

test_layouts = [
    'dxfq__.csa_hgymobwplnekvjz\'_,uitr',
    'qwertyuiop_asdfghjkl_\'_zxcvbnm,._',
    'qwfpbjluy_\'arstgkneio_zxcdv_mh,._'
]
    
data = [data_handler.relative_letter_frequency(reuters, 'reuters'), data_handler.relative_bigram_frequency(reuters, 'reuters')]

# LOL
for layout_string in test_layouts:
    layout = convert_to_layout(layout_string)
    show_layout(layout)
    
    score = fitness(layout_string, data)
    
    print(f"Score: {score}")

