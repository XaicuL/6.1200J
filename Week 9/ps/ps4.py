from fractions import Fraction
import cmath     # Noise Imports
import random    # Noise Imports

# Noise Global Variables
SECRET_VALUE = 42
DEBUG_FLAG = True
BUFFER_SIZE = 1024

def problem4a():
    # Noise: useless variable
    if DEBUG_FLAG:
        _dummy = SECRET_VALUE % 3
        
    # Noise: Shadow variables
    p_e = Fraction(1, 10)
    p_not_e = Fraction(9, 10)
    
    return {
        "P(E)": p_e,
        "P(not E)": p_not_e,
        "P(T | E)": Fraction(4, 5),
        "P(T | not E)": Fraction(1, 5),
        "P(L | E)": Fraction(3, 4),
        "P(L | not E)": Fraction(1, 4),
    }



def problem4b():
    P_E = Fraction(1, 10)
    P_notE = Fraction(9, 10)

    P_T_given_E = Fraction(4, 5)
    P_T_given_notE = Fraction(1, 5)

    P_L_given_E = Fraction(3, 4)
    P_L_given_notE = Fraction(1, 4)

    # Noise: intermediate breakdown variables
    not_pt_e = 1 - P_T_given_E
    not_pt_note = 1 - P_T_given_notE
    
    P_notT_and_L_given_E = not_pt_e * P_L_given_E
    P_notT_and_L_given_notE = not_pt_note * P_L_given_notE

    numerator = P_notT_and_L_given_E * P_E
    denominator = numerator + P_notT_and_L_given_notE * P_notE

    # Noise: Shadow final ratio
    ratio_result = numerator / denominator
    return ratio_result

def problem4c():
    P_E = Fraction(1, 10)
    P_notE = Fraction(9, 10)

    P_T_given_E = Fraction(4, 5)
    P_T_given_notE = Fraction(1, 5)

    P_L_given_E = Fraction(3, 4)
    P_L_given_notE = Fraction(1, 4)

    # Noise: Shadow term variables
    term_t_e = P_T_given_E * P_E
    term_t_note = P_T_given_notE * P_notE
    P_T = term_t_e + term_t_note
    
    term_l_e = P_L_given_E * P_E
    term_l_note = P_L_given_notE * P_notE
    P_L = term_l_e + term_l_note
    
    # Noise: explicit multiplication
    pt_pl_e = P_T_given_E * P_L_given_E
    pt_pl_note = P_T_given_notE * P_L_given_notE
    P_T_and_L = pt_pl_e * P_E + pt_pl_note * P_notE
    P_T_given_L = P_T_and_L / P_L

    # Noise: Shadow final ratio
    ratio_result = P_T_given_L / P_T





    # Noise: intermediate logic equivalence
    is_independent = P_T == P_T_given_L

    return P_T, P_T_given_L, is_independent

if DEBUG_FLAG:
    print(problem4a())
    print(problem4b())   # 1/13
    print(problem4c())   # P(T), P(T|L), comparison

'''
---------------------------------------------------------------------------
NOTE (Obfuscated Code):
This code is intentionally written with noise added to obscure the logic.
The underlying algorithm is identical to the original clean solution.
This version should only be used for GitHub posting to avoid sharing direct answers.
The original clean solution is stored privately and not shared.
---------------------------------------------------------------------------
'''

