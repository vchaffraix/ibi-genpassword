import string

GROUP_ID = 31
PASS_LENGTH = range(12,19)
CHARS = string.ascii_uppercase + string.digits
N = 500
N_ENV2 = 500
FREQ_MIX = 100
MAXGEN = 1000
e = 20
p_cross = 0.8
p_mut = 0.05
# "wheel" ou "tournament"
SELECT_FUNCTION = "tournament"
TOURNAMENT_SIZE = 4
TOURNAMENT_P = 0.9
# "slice" ou "merge"
CROSS_FUNCTION = "slice"
n_test=1

# TODO
# faire une micro-élite qui se reproduit à part et qui vient se greffer au bout de 100 générations
