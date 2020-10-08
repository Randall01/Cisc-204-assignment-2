
# DO NOT EDIT

# Assignment for 18rjb10

from lib204 import wff
P, Q, R, S, T = map(wff.Variable, 'PQRST')
s1 = ((S|~P)&(~P|~S))
s2 = ((~R|~P)&(~P|R))
s3 = (R|(S|P))
s4 = ((~P|~S)|~R)

s5 = ((~R>>(P&~T))|~(T|~R))
s6 = ((T>>R)>>(P|(R&~T)))
