import pandas as pd
import numpy as np
from visualize import draw_map

df = pd.read_csv("places.csv")
places = []
for row in df.itertuples():
    places.append([row[2], (row[3], row[4])])
print(places)
draw_map(places)
