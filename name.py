import pandas as pd
import matplotlib.pyplot as plt

# CSV file read
df = pd.read_csv('Amna-AI-Course-Bin/Untitled 2.csv')

# Bar chart draw
plt.figure()
plt.bar(df['Task'], df['Duration'])
plt.xlabel("Task")
plt.ylabel("Duration (Days)")
plt.title("FYP Project Duration")
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()
