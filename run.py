
from lib204 import wff, semantic_interface
#import test 

try:
    from config import *
except:
    try:
        from .config import *
    except:
        print("\n\tYou must download your config.py file first. See the assignment details in OnQ.\n")
        exit(1)



# First step: run this file (python run.py), and see the output.
print('\nFormulae for Question 1:')
print(" s1: %s" % s1)
print(" s2: %s" % s2)
print(" s3: %s" % s3)
print(" s4: %s" % s4)

print('\nFormulae for Question 2:')
print(" s5: %s" % s5)
print(" s6: %s" % s6)

################################################################################
# Question 1
#  Given the following logical sentences,
#   (a) write the truth table for each of them,
#    S  P  R | ((S∨¬P)∧(¬P∨¬S)) | ((¬R∨¬P)∧(¬P∨R)) | (R∨(S∨P)) | ((¬P∨¬S)∨¬R)
#   -------------------------------------------------------------------------------------- 
#    T  T  T |   T   F  ∴  F    |   F   T   ∴  F   |  T  ∴  T  |  F  F  ∴  F 
#    T  T  F |   T   F  ∴  F    |   T   F   ∴  F   |  T  ∴  T  |  F  T  ∴  T 
#    T  F  T |   T   T  ∴  T    |   T   T   ∴  T   |  T  ∴  T  |  T  F  ∴  T 
#    T  F  F |   T   T  ∴  T    |   T   T   ∴  T   |  T  ∴  T  |  T  T  ∴  T 
#    F  T  T |   F   T  ∴  F    |   F   T   ∴  F   |  T  ∴  T  |  T  F  ∴  T 
#    F  T  F |   F   T  ∴  F    |   T   F   ∴  F   |  T  ∴  T  |  T  T  ∴  T 
#    F  F  T |   T   T  ∴  T    |   T   T   ∴  T   |  F  ∴  T  |  T  F  ∴  T 
#    F  F  F |   T   T  ∴  T    |   T   T   ∴  T   |  F  ∴  F  |  T  T  ∴  T
#   (b) determine which ones are equivalent (i.e., have the same truth table),
#      ((S∨¬P)∧(¬P∨¬S)) ≡ ((¬R∨¬P)∧(¬P∨R))
#   (c) find a model satisfied by one formula, but none of the others
#      S = T, P = T, R = T, 
#      s1 = F, s2 = F, s3 = T, s4 = F 

# (a) Put the truth tables (text file, written on paper + picture, whatever)
#     into the Q1a folder

# (b) Variable q1b should be a list of lists that group together the equivalent
#     theories. These are two wrong answers, but they give you an idea of how
#     to write your response.

#q1b = [ [s1,s2,s3,s4] ] # they are all equivalent.
#q1b = [ [s1], [s2], [s3], [s4] ] # they are all different
q1b = [ [s1,s2], [s3], [s4]] # the right answer please!

# (c) Variable q1c should be a dictionary mapping variables to True or False.
#     Use only what you need of P, Q, R, S, T. An example (almost certainly
#     incorrect) answer is given as an example.
q1c = {
    P: True,
    Q: True,
    R: True,
    S: True,
    T: True
}



################################################################################
# Question 2
# Given the following logical sentences,
#  (a) [optional, but recommended] write the parse tree for each of them
#              ∨                                 → 
#           /     \                           /     \
#          →       ¬                         →       ∨ 
#        /   \     |                        / \     / \
#       ¬    ∧     ∨                       T   R   P   ∧ 
#       |   / \   / \                                 / \
#       R  P   T T   ¬                               R   ¬ 
#                    |                                   |
#                    R                                   T
#
#  (b) convert them to negation normal form
# s5 = ((¬R→(P∧¬T))∨¬(T∨¬R))     s6 = ((T→R)→(P∨(R∧¬T)))
#    = ((¬R→(P∧¬T))∨(¬T∧¬¬R))    s6 = ((¬T∨R)→(P∨(R∧¬T)))
#    = ((¬R→(P∧¬T))∨(¬T∧R))      s6 = (¬(¬T∨R)∨(P∨(R∧¬T)))
#    = ((¬¬R∨(P∧¬T))∨(¬T∧R))     s6 = ((¬¬T∧¬R)∨(P∨(R∧¬T)))
#    = ((R∨(P∧¬T))∨(¬T∧R))       s6 = ((T∧¬R)∨(P∨(R∧¬T)))
#  (c) convert them to CNF using distribution and de Morgan's rules
# s5 = ((R∨(P∧¬T))∨(¬T∧R))                                 s6 = ((T∧¬R)∨(P∨(R∧¬T)))
# s5 = (((R∨P)∧(R∨¬T))∨(¬T∧R))                             s6 = ((T∨(P∨(R∧¬T)))∧(¬R∨(P∨(R∧¬T))))               
# s5 = (((R∨P)∨(¬T∧R))∧((R∨¬T)∨(¬T∧R)))                    s6 = ((T∨((P∨R)∧(P∨¬T)))∧(¬R∨((P∨R)∧(P∨¬T))))
# s5 = ((((R∨P)∨¬T)∧((R∨P)∨R))∧(((R∨¬T)∨¬T)∧((R∨¬T)∨R)))   s6 = ((T∨(P∨R))∧(T∨(P∨¬T))∧(¬R∨(P∨R))∧(¬R∨(P∨¬T)))
# s5 = ((R∨P∨¬T)∧(R∨¬T)∧(R∨P))                                                *always True*
#                                                           s6 = ((R∨P∨T)∧(¬T∨P∨¬R))
#                              
#  (d) encode them using the Tseitin encoding
# s5 = ((¬R→(P∧¬T))∨¬(T∨¬R))   s6 = ((T→R)→(P∨(R∧¬T)))
# X1 ⟷ (¬R)                   X1 ⟷ (¬T)
# X2 ⟷ (P∧T)                  X2 ⟷ (R∧X1)
# X3 ⟷ (¬R)                   X3 ⟷ (T→R)
# X4 ⟷ (T∨X3)                 X4 ⟷ (P∨X2)
# X5 ⟷ (X1→X2)                X5 ⟷ (X3→X4)
# X6 ⟷ (¬X4)                 
# X7 ⟷ (X5∨X6)                

print("\n\nCopy these two lines for Question 2:")
print("s5 = %s" % s5.dump('python'))
print("s6 = %s" % s6.dump('python'))
#s5 = ((~R>>(P&~T))|~(T|~R))
#s6 = ((T>>R)>>(P|(R&~T)))
#

# replace the following two lines with what the above code prints
s5 = ((~R>>(P&~T))|~(T|~R))
s6 = ((T>>R)>>(P|(R&~T)))

# (a) Put the parse trees inside folder Q2a. You can do it on paper and take a
#     photo, or use drawing software. This will not be marked unless requested,
#     but the quiz will ask a similar question that /will/ be marked.

# (b) Copy s5 and s6 formulae into the first steps below, and show the steps to
#     convert to negation normal form. An example is given, but it is the wrong
#     starting formula. You /must/ provide an explanation for each step. Possible
#     explanations might include (exact wording is not required)...
#      - starting formula
#      - de Morgans
#      - distribution
#      - replace implications
#      - double negation
#      - etc.

s5nnf = [
    [(((~R) >> (P & (~T))) | (~(T | (~R)))),'starting formula'],
    [(((~R) >> (P & (~T))) | ((~T) & (~~R))), 'de Morgans'],
    [(((~R) >> (P & (~T))) | ((~T) & R)) , 'Double negation'],
    [(((~~R) | (P & (~T))) | ((~T) & R)), 'replace implications '],
    [((R | (P & (~T))) | ((~T) & R)), ' double negation']
]

s6nnf = [
    [((T >> R) >> (P | (R & (~T)))),'Starting Formula '],
    [(((~T) | R) >> (P | (R & (~T)))),'replace implications '],
    [((~((~T) | R)) | (P | (R & (~T)))),'replace implications '],
    [(((~~T) & (~R)) | (P | (R & (~T)))), 'de Morgans'],
    [((T & (~R)) | (P | (R & (~T)))), 'double negation ']
]


# (c) Copy s5 and s6 formulae into the first steps below, and show the steps to
#     convert to CNF using distribution, de Morgan's, implication removal, etc.
#     An example is given, but it is for the wrong formula. You /must/ provide
#     an explanation for each step. Possible explanations are listed above.

s5cnf = [
    [(((~R) >> (P & (~T))) | (~(T | (~R)))),'starting formula'],
    [(((~R) >> (P & (~T))) | ((~T) & (~~R))), 'de Morgans'],
    [(((~R) >> (P & (~T))) | ((~T) & R)) , 'Double negation'],
    [(((~~R) | (P & (~T))) | ((~T) & R)), 'replace implications '],
    [((R | (P & (~T))) | ((~T) & R)), ' double negation'],
    [(((R | P) & (R | (~T))) | ((~T) & R)), 'distribution '],
    [(((R | P) | ((~T) & R)) & ((R | (~T)) | ((~T) & R))),'distribution '],
    [((((R | P) | (~T)) & ((R | P) | R)) & (((R | (~T)) | (~T)) & ((R | (~T)) | R))), ' distribution'],
    [((R | P | (~T)) & (R | (~T)) & (R | P)), ' remove repititions  ']
]

s6cnf = [
    [((T >> R) >> (P | (R & (~T)))),'Starting Formula '],
    [(((~T) | R) >> (P | (R & (~T)))),'replace implications '],
    [((~((~T) | R)) | (P | (R & (~T)))),'replace implications '],
    [(((~~T) & (~R)) | (P | (R & (~T)))), 'de Morgans'],
    [((T & (~R)) | (P | (R & ((~T))))), 'double negation '],
    [((T | (P | (R & (~T)))) & ((~R) | (P | (R & (~T))))), 'distribution'],
    [((T | ((P | R) & (P | (~T)))) & ((~R) | ((P | R) & (P | (~T))))), 'distribution '],
    [((T | (P | R)) & (T | (P | (~T))) & ((~R) | (P | R)) & ((~R) | (P | (~T)))), 'distribution'],
    [((R | P | T) & ((~T) | P | (~R))), 'remove repititions']
]


# (d) Build the Tseitin encoding of both s5 and s6 using the semantic_interface
#     library to create auxiliary variables as necessary. Examples for different
#     formulae are given. There is a limit of one operator per auxiliary variable,
#     and you may re-use auxiliary variables as necessary.

# e.g., s5 = ~(P | Q)
s5tseitin = semantic_interface.Encoding()
# first argument is the formula; second is the variable name.
x1 = s5tseitin.tseitin(~R, 'x1')
x2 = s5tseitin.tseitin(P&T, 'x2')
x3 = s5tseitin.tseitin(~R, 'x3')
x4 = s5tseitin.tseitin(T|x3, 'x4')
x5 = s5tseitin.tseitin(x1>>x2, 'x5')
x6 = s5tseitin.tseitin(~x4, 'x6')
x7 = s5tseitin.tseitin(x5|x6, 'x7')

# This final step is required -- use your last variable, corresponding to the top
#  of the parse tree, to finalize your Tseitin encoding.
s5tseitin.finalize(x7)

# e.g., s6 = (P & Q) | R
s6tseitin = semantic_interface.Encoding()
x1 = s6tseitin.tseitin(~T, 'x1')
x2 = s6tseitin.tseitin(R&x1, 'x2')
x3 = s6tseitin.tseitin(T>>R, 'x3')
x4 = s6tseitin.tseitin(P|x2, 'x4')
x5 = s6tseitin.tseitin(x3>>x4, 'x5')

s6tseitin.finalize(x5)

print()
if __name__ == "__main__":
    from test import test_submission
    test_submission()
