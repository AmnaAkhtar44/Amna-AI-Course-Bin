import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.DataFrame({'house_size' : np.arange(100) , 'price' : np.random.rand(100).cumsum()})

sns.lineplot(x = 'house_size' , y = 'price' , data=data)
plt.show()
# hue bed kind scatter
sns.set_theme(style = 'whitegrid')
sns.lineplot(x = 'house_size' , y = 'price' , data = data)
plt.show()
sns.set_theme(style = 'darkgrid')
sns.lineplot(x = 'house_size' , y = 'price' , data = data)
plt.show()
sns.set_theme(style='dark')
sns.lineplot(x = 'house_size' , y = 'price' , data = data )
plt.show()
sns.set_theme(style= 'white')
sns.lineplot(x = 'house_size' , y = 'price' , data = data)
plt.show()
sns.set_theme(style='ticks')
sns.lineplot(x = 'house_size' , y = 'price' , data = data)
plt.show()

#customising theme
sns.set_theme(style = 'darkgrid' , rc = {'axes.facecolor': 'grey' , 'grid.color' :'white'})
sns.lineplot( x = 'house_size' , y = 'price' , data = data)
plt.show()

# Load data from a CSV file
df = pd.read_csv('Amna-AI-Course-Bin/PandasPractice/RealEstate-USA (1).csv',delimiter=",")
print(df.dtypes)
dffilter= df.head(40)
dffilter100= df.head(100)

sns.set(style="whitegrid")
g=sns.displot(data=dffilter, x="house_size" , y="price" , hue="bed",  kind='hist'  )
g.figure.suptitle("sns.displot(data=dffilter, x='house_size', y='price', hue='bed',  kind='hist'  )"  )

# Display the plot
g.figure.show()
read = input("Wait for me....")
#g.figure.clear()

#kind='kde'
g=sns.displot(data=dffilter, x='house_size', y='price', kind='kde'  )
g.figure.suptitle("sns.displot(data=dffilter, x='house_size', y='price' , kind='kde'  )"  )

# Display the plot
g.figure.show()
read = input("Wait for me....")
#g.figure.clear()

#kind='kde'
g=sns.kdeplot(data=dffilter, x="house_size")
g.figure.suptitle("sns.kdeplot(data=dffilter, x=house_size)"  )

# Display the plot
g.figure.show()
read = input("Wait for me....")
#g.figure.clear()

g = sns.histplot(data=dffilter, x='agency', y='price', hue='bed', multiple="stack")
g.figure.suptitle("sns.histplot(data=dffilter, x='agency', y='price', hue='bed', multiple=stack)"  )
# Display the plot
g.figure.show()
read = input("Wait for me....")
#g.figure.clear()

# Use Seaborn to create a plot
g = sns.scatterplot(x='house_size', y='price', data=dffilter)
g.figure.suptitle("sns.scatterplot(x='house_size', y='price', data=dffilter)"  )
g.figure.show()
read = input("Wait for me....")
#g.figure.clear()

g=sns.lineplot(data=dffilter, x='house_size', y='price' )
g.figure.suptitle("sns.lineplot(data=dffilter, x=house_size , y=price  )"  )
# Display the plot
g.figure.show()
read = input("Wait for me....")
#g.figure.clear()

g=sns.barplot(data=dffilter, x="house_size", y="price", legend=False)
g.figure.suptitle("sns.barplot(data=dffilter, x=house_size, y=price, legend=False)"  )
# Display the plot
g.figure.show()
read = input("Wait for me....")
#g.figure.clear()

g=sns.catplot(data=dffilter, x="house_size", y="price")
g.figure.suptitle("sns.catplot(data=df, x=house_size, y=price)"  )
# Display the plot
g.figure.show() 
read = input("Wait for me....")
#g.figure.clear()

#.pivot(index="Model", columns="agency", values="price")
glue = dffilter.pivot(columns="house_size", values="price")

g=sns.heatmap(glue)
g.figure.suptitle("sns.heatmap(glue)  - glue = dffilter.pivot(columns=house_size, values=price)"  )
# Display the plot
g.figure.show()
read = input("Wait for me....")
#g.figure.clear()
