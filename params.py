import string

GROUP_ID = 31
PASS_LENGTH = range(12,19)
CHARS = string.ascii_uppercase + string.digits
N = 500
MAXGEN = 1000
e = 10
p_cross = 0.7
p_mut = 0.04
# "wheel" ou "tournament"
SELECT_FUNCTION = "tournament"
TOURNAMENT_SIZE = 8
TOURNAMENT_P = 0.8
# "slice" ou "merge"
CROSS_FUNCTION = "slice"
