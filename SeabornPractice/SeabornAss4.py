import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.DataFrame({'city' : np.arange(100) , 'price' : np.random.rand(100).cumsum()})

sns.lineplot(x = 'city' , y = 'price' , data=data)
plt.show()
# hue bed kind scatter
sns.set_theme(style = 'whitegrid')
sns.lineplot(x = 'city' , y = 'price' , data = data)
plt.show()
sns.set_theme(style = 'darkgrid')
sns.lineplot(x = 'city' , y = 'price' , data = data)
plt.show()
sns.set_theme(style='dark')
sns.lineplot(x = 'city' , y = 'price' , data = data )
plt.show()
sns.set_theme(style= 'white')
sns.lineplot(x = 'city' , y = 'price' , data = data)
plt.show()
sns.set_theme(style='ticks')
sns.lineplot(x = 'city' , y = 'price' , data = data)
plt.show()

#customising theme
sns.set_theme(style = 'darkgrid' , rc = {'axes.facecolor': 'grey' , 'grid.color' :'white'})
sns.lineplot( x = 'city' , y = 'price' , data = data)
plt.show()

# Load data from a CSV file
df = pd.read_csv('Amna-AI-Course-Bin/Week4/zameencom-property-data-By-Kaggle-Short.csv',delimiter=";")
print(df.dtypes)
dffilter= df.head(40)
dffilter100= df.head(100)

sns.set(style="whitegrid")
g=sns.displot(data=dffilter, x="city" , y="price" , hue="purpose",  kind='hist'  )
g.figure.suptitle("sns.displot(data=dffilter, x='city', y='price', hue='purpose',  kind='hist'  )"  )

# Display the plot
g.figure.show()
read = input("Wait for me....")
#g.figure.clear()

#kind='kde'
g=sns.displot(data=dffilter, x='city', y='price', kind='kde'  )
g.figure.suptitle("sns.displot(data=dffilter, x='city', y='price' , kind='kde'  )"  )

# Display the plot
g.figure.show()
read = input("Wait for me....")
#g.figure.clear()

#kind='kde'
g=sns.kdeplot(data=dffilter, x="city")
g.figure.suptitle("sns.kdeplot(data=dffilter, x=city)"  )

# Display the plot
g.figure.show()
read = input("Wait for me....")
#g.figure.clear()

g = sns.histplot(data=dffilter, x='city', y='price', hue='purpose', multiple="stack")
g.figure.suptitle("sns.histplot(data=dffilter, x='city', y='price', hue='purpose', multiple=stack)"  )
# Display the plot
g.figure.show()
read = input("Wait for me....")
#g.figure.clear()

# Use Seaborn to create a plot
g = sns.scatterplot(x='city', y='price', data=dffilter)
g.figure.suptitle("sns.scatterplot(x='city', y='price', data=dffilter)"  )
g.figure.show()
read = input("Wait for me....")
#g.figure.clear()

g=sns.lineplot(data=dffilter, x='city', y='price' )
g.figure.suptitle("sns.lineplot(data=dffilter, x=city , y=price  )"  )
# Display the plot
g.figure.show()
read = input("Wait for me....")
#g.figure.clear()

g=sns.barplot(data=dffilter, x="city", y="price", legend=False)
g.figure.suptitle("sns.barplot(data=dffilter, x=city, y=price, legend=False)"  )
# Display the plot
g.figure.show()
read = input("Wait for me....")
#g.figure.clear()

g=sns.catplot(data=dffilter, x="city", y="price")
g.figure.suptitle("sns.catplot(data=df, x=city, y=price)"  )
# Display the plot
g.figure.show() 
read = input("Wait for me....")
#g.figure.clear()

#.pivot(index="Model", columns="agency", values="price")
glue = dffilter.pivot(columns="city", values="price")

g=sns.heatmap(glue)
g.figure.suptitle("sns.heatmap(glue)  - glue = dffilter.pivot(columns=city, values=price)"  )
# Display the plot
g.figure.show()
read = input("Wait for me....")
#g.figure.clear()
