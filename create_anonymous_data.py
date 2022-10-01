import pandas as pd
from local_functions import *
from sklearn.preprocessing import minmax_scale
import sys

verbruik = read_eneco_usage(sys.argv[1])
verbruik[:] = minmax_scale(verbruik[:])
verbruik.to_excel('data/usage_anonymized.xlsx')