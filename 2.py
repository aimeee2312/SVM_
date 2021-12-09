import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

names = ['sepal-length', 'sepal-width','petal-lenth','petal-width','Class']
dataset = pd.read_csv(url=names)

dataset.head()