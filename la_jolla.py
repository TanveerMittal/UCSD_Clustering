import pandas as pd
import numpy as np
from visualize import draw_map

df = pd.read_csv("places.csv")
places = [[row[2], (row[3], row[4])] for row in df.itertuples()]
draw_map(places)
