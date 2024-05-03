
from utils import convert_to_layout, show_layout
from formulas import fitness
import data_handler
from nltk.corpus import reuters

layout_string = 'dxfq__.csa_hgymobwplnekvjz\'_,uitr'
layout = convert_to_layout(layout_string)
show_layout(layout)

# ====== Generation 922: qxj__.,ac__gkdmshblpnevfzyt'wuior - Score: 10500.173068545553 ======
# dxfq__.csa_hgymobwplnekvjz'_,uitr
# ====== Generation 265: eta.__,kzv_'lpouyfhgsnmcirb_jqxwd - Score: 13871.278324919605 ======
# ====== Generation 221: xjy,__.tpn_'dhguibelsazfwqv_krmco - Score: 13884.097187005522 ======
# ====== Generation 219: qfkz__.ibs_hylmnucadpevjgx'_,wrto - Score: 14048.06060043876 ======
#  "vzmk__,gao_fhtlruipsdnyxqj'_.wcbe",
#"kfjx__.tmb_rayolgwhpesvndzq_u,ic'",
#"kxj.q_ebca_dvygmulwpstfhz,'_o_nri",
#"anup__.ojq_elcwitmdsvfryb,'_xghzk",
#"uso.__vfkz_aecbmwydnplhgrti_q,j'x",
#"ofjx__,bns_lhymkuirtcpgvz.q_weda'",
#"zfqk__alr__dhyucsgbnmivxj,.'etopw",
#"ubr,__.xoj_ngacmiwvdyfpsle_'kzhtq",
#"kzq,__.eol_abvmwurptnsfjxy'_gicdh",
#"qkmj_.,ci__ypdlfoweasnvhxz_'burtg",

# GEN 2
#"vzmk__,gao_fhtlruipsdnyxqj'_.wcbe",
#"kfjx__.tmb_rayolgwhpesvndzq_u,ic'",
#"kxj.q_ebca_dvygmulwpstfhz,'_o_nri",
#"anup__.ojq_elcwitmdsvfryb,'_xghzk",
#"uso.__vfkz_aecbmwydnplhgrti_q,j'x",
#"ofjx__,bns_lhymkuirtcpgvz.q_weda'",
#"zfqk__alr__dhyucsgbnmivxj,.'etopw",
#"ubr,__.xoj_ngacmiwvdyfpsle_'kzhtq",
#"kzq,__.eol_abvmwurptnsfjxy'_gicdh",
#"qkmj_.,ci__ypdlfoweasnvhxz_'burtg",

#"lnd,__qfgz_cibsrtmyhoveapwu_.k'jx",
#"kvzj_,.ai__gldymbcnepshfxq'_wurto",
#"ydzq__,btr_hgfkmwcnpslvojx'_.uaei",

# Using tournament selection
#"gpvz_lrmihocsbdjfyaeunkxtq'_.,_w_"
#"m,bjx_gsi'_ofhkzplnwyaqtc.u_erd_v"
#"ser._',clq_mbdnoypxvkthaigu__zjwf"

#"gpvz_lrmihocsbdjfyaeunkxtq'_.,_w_",
#"m,bjx_gsi'_ofhkzplnwyaqtc.u_erd_v",
#"ser._',clq_mbdnoypxvkthaigu__zjwf",

#"gqjx__.hei_nmdktublpsafyzv_',worc",
#"djkq__,rht_pgovmwilsnafyzx_'.ubec",
#"ngsr_,.jxk_pbcultmyvhoidea__qwz'f",
#"ipn,__.zxv_ldcuwtmoyhgarbse_qk'jf",

# =================================
# Changing broken fitness function somewhere here...

#"n_hvskqo're.lgzxbjpdu_at_mwcfy,i_",

#"j'wdhfeuzb_gkitnoas,r_xq_ylmpc.v_",
#"xdfq__ulcw_ateoyhnirsbpvmzj_.,'kg",

# Looks ok? "fcl.,_qdyz_sntrgvoaeihmupbw_x_kj'"

# Gen 3 combination workload distribution
#"khp.__wydx_nsirclteaofmbug_',qzvj",

test_layouts = [
    'qwertyuiop_asdfghjkl_\'_zxcvbnm,._',
    'qwfpbjluy_\'arstgkneio_zxcdv_mh,._',
    "bdl,__.fyq_irnscmteaovpwhu_'gkjzx",
    "bcl.,_qdfx_nrsihyteaopmwgu__vj'kz",
    "bcl.,'xdyq_isnrhpaetofmgwu__v_zjk",
    "wdl,__qhfx_iseacmtrnoygbpu'_.vzjk"
]
    
data = [data_handler.relative_letter_frequency(reuters, 'reuters'), data_handler.relative_bigram_frequency(reuters, 'reuters')]

print(data)

# LOL
for layout_string in test_layouts:
    layout = convert_to_layout(layout_string)
    show_layout(layout)
    
    score = fitness(layout_string, data)
    
    print(f"Score: {score}")

