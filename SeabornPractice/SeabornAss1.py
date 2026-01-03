import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# Sample data
data = pd.DataFrame({'province': np.arange(100), 'latitude': np.random.rand(100).cumsum()})

# Set the theme
sns.set_theme(style='darkgrid')
# Alternatively
# sns.set_style('darkgrid')

# Create a plot # we can also attach pd.csv file 
sns.lineplot(x='province', y='latitude', data=data)
plt.show()

# Other themes can be set similarly
sns.set_theme(style='whitegrid')
sns.lineplot(x='province', y='latitude', data=data)
plt.show()

sns.set_theme(style='dark')
sns.lineplot(x='province', y='latitude', data=data)

plt.show()

sns.set_theme(style='white')
sns.lineplot(x='province', y='latitude', data=data)
plt.show()

sns.set_theme(style='ticks')
sns.lineplot(x='province', y='latitude', data=data)
plt.show()


# Customize the  theme # we can overwrite things using rc dictionary
sns.set_theme(style='darkgrid', rc={'axes.facecolor': 'grey', 'grid.color': 'white'})

# Create a plot
sns.lineplot(x='province', y='latitude', data=data)
plt.show()


#Zameencom data - based examples
# Load data from a CSV file
df = pd.read_csv(r'Amna-AI-Course-Bin/NumpyPractice/FastFoodRestaurants (1).csv',delimiter=",", index_col='latitude')

print(df.dtypes)
dffilter= df.head(40)
dffilter100= df.head(100)


sns.set(style="whitegrid")

#kind='hist'  
g=sns.displot(data=dffilter, x="province" , y="latitude" , hue="city",  kind='hist'  )
g.figure.suptitle("sns.displot(data=dffilter, x=province , y=latitude , hue=city,  kind='hist'  )"  )

# Display the plot
g.figure.show()
read = input("Wait for me....")
#g.figure.clear()


#kind='kde'
g=sns.displot(data=dffilter, x="province" , y="latitude" , kind='strip'  )
g.figure.suptitle("sns.displot(data=dffilter, x=province , y=latitude , kind='strip'  )"  )

# Display the plot
g.figure.show()
read = input("Wait for me....")
#g.figure.clear()

#kind='kde'
g=sns.kdeplot(data=dffilter, x="province")
g.figure.suptitle("sns.kdeplot(data=dffilter, x=province)"  )

# Display the plot
g.figure.show()
read = input("Wait for me....")
#g.figure.clear()


g = sns.histplot(data=dffilter, x='province', y='latitude', hue='city', multiple="stack")
g.figure.suptitle("sns.histplot(data=dffilter, x='province', y='latitude', hue='city', multiple=stack)"  )
# Display the plot
g.figure.show()
read = input("Wait for me....")
#g.figure.clear()


# Use Seaborn to create a plot
g = sns.scatterplot(x='province', y='latitude', data=dffilter)
g.figure.suptitle("sns.scatterplot(x='province', y='latitude', data=dffilter)"  )
g.figure.show()
read = input("Wait for me....")
#g.figure.clear()


#raphics more accessible."""
g=sns.lineplot(data=dffilter, x="province" , y="latitude"  )
g.figure.suptitle("sns.lineplot(data=dffilter, x=province , y=latitude  )"  )
# Display the plot
g.figure.show()
read = input("Wait for me....")
#g.figure.clear()




g=sns.barplot(data=dffilter, x="province", y="latitude", legend=False)
g.figure.suptitle("sns.barplot(data=dffilter, x=province, y=latitude, legend=False)"  )
# Display the plot
g.figure.show()
read = input("Wait for me....")
#g.figure.clear()



g=sns.catplot(data=dffilter, x="province", y="latitude")
g.figure.suptitle("sns.catplot(data=df, x=province, y=price)"  )
# Display the plot
g.figure.show() 
read = input("Wait for me....")
#g.figure.clear()

#.pivot(index="Model", columns="agency", values="price")
glue = dffilter.pivot(columns="latitude", values="province")

g=sns.heatmap(glue)
g.figure.suptitle("sns.heatmap(glue)  - glue = dffilter.pivot(columns=latitude, values=province)"  )
# Display the plot
g.figure.show()
read = input("Wait for me....")
#g.figure.clear()