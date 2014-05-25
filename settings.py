#encoding: UTF-8

"""Settings.py
Sets all parameters and constants used in the simulation.
"""

# -- TIME --
STEP_SIZE = 1

# -- STATISTICS --
RANDOM_SEED = 42         # default is 42, controls random number generation
PARETO_SHAPE = 0.670     # from Goddard, 2014 [1]
PARETO_SCALE = 2994218   # [1]
LOGNORMAL_MEAN = 11.910  # [1]
LOGNOMRAL_STDEV = 1.078  # [1]

# -- BANK NETWORK --
NUMBER_OF_BANKS_LOGNORMAL = 6300  # As in the 2014 paper by Goddard on the asset size distribution of the
NUMBER_OF_BANKS_PARETO = 180      # US banking market. [1] +/- 180 banks control 85% of all assets.
POWERLAW_PARAMETER = 3

# -- BALANCE SHEET --
DEFAULT_CONSUMER_LOANS_FRACTION = 0.5
DEFAULT_CASH_FRACTION = 0.07
DEFAULT_DEPOSITS_FRACTION = 0.70
DEFAULT_EQUITY_FRACTION = 0.075

# -- DATA --
DATA_FILE = 'path/to/data.csv'

# -- CODE_SPECIFIC REFERENCES --
# As mentioned in comments and docstrings:
#
# [1] J. Goddard, H. Liu, D. Mckillop, and J. O. S. Wilson, “The Size Distribution of US Banks and Credit Unions,”
#        Int. J. Econ. Bus., vol. 21, no. 1, pp. 139–156, Jan. 2014.
#
# [2] A. Krause and S. Giansante, “Interbank lending and the spread of bank failures: A network model of systemic risk,”
#        J. Econ. Behav. Organ., vol. 83, no. 3, pp. 583–608, 2012.
#
# [3] R. Gropp and F. Heider, “The Determinants of Bank Capital Structure,” Rev. Financ., vol. 14, no. 4, pp. 587–622,
#        Mar. 2010.






