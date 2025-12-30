import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings as wr
wr.filterwarnings('ignore')

df = pd.read_csv("/content/WineQT.csv")
print(df.head())

df.shape
df.info()
df.describe().T
df.columns.tolist()
df.isnull().sum()
df.nunique()
