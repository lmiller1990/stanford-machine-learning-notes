import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('TripAdvisorReviews.csv', sep = ';')

print(df.describe())
