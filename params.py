import string

GROUP_ID = 31
PASS_LENGTH = range(12,19)
CHARS = string.ascii_uppercase + string.digits
N = 500
MAXGEN = 1000
e = 10
p_cross = 0.8
p_mut = 0.05
C_max = 1
# "wheel" ou "tournament"
SELECT_FUNCTION = "tournament"
TOURNAMENT_SIZE = 4
TOURNAMENT_P = 0.9
# "slice" ou "merge"
CROSS_FUNCTION = "slice"
