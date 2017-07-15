import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('lake_track_waypoints.csv')
plt.plot(df['x'], df['y'])
plt.show()