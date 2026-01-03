import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
data = pd.DataFrame({'City' : np.arange(100) , 'Valuation ($B)' : np.random.rand(100).cumsum()})
sns.lineplot(x = 'City' , y = 'Valuation ($B)' , data=data)
plt.show()
# hue bed kind scatter
sns.set_theme(style = 'whitegrid')
sns.lineplot(x = 'City' , y = 'Valuation ($B)' , data = data)
plt.show()
sns.set_theme(style = 'darkgrid')
sns.lineplot(x = 'City' , y = 'Valuation ($B)' , data = data)
plt.show()
sns.set_theme(style='dark')
sns.lineplot(x = 'City' , y = 'Valuation ($B)' , data = data )
plt.show()
sns.set_theme(style= 'white')
sns.lineplot(x = 'City' , y = 'Valuation ($B)' , data = data)
plt.show()
sns.set_theme(style='ticks')
sns.lineplot(x = 'City' , y = 'Valuation ($B)' , data = data)
plt.show()

#customising theme
sns.set_theme(style = 'darkgrid' , rc = {'axes.facecolor': 'grey' , 'grid.color' :'white'})
sns.lineplot( x = 'City' , y = 'Valuation ($B)' , data = data)
plt.show()

# Load data from a CSV file
df = pd.read_csv('Amna-AI-Course-Bin/PandasPractice/Startups in 2021 end.csv',delimiter=",")
print(df)
print(df.dtypes)
data = df.head(50)
dffilter= df.head(40)
dffilter100= df.head(100)

df['Valuation ($B)'] = df['Valuation ($B)'].str.replace('$','')
print(df['Valuation ($B)'])
print(df)
df['Valuation ($B)'] = df['Valuation ($B)'].astype(float)
print(df.dtypes)

print(df)

sns.set(style="whitegrid")
g=sns.displot(data=dffilter, x="City" , y="Valuation ($B)" , hue="Country",  kind='hist'  )
g.figure.suptitle("sns.displot(data=dffilter, x='City', y='Valuation ($B)', hue='Country',  kind='hist'  )"  )

# Display the plot
g.figure.show()
read = input("Wait for me....")
#g.figure.clear()

#kind='kde'
g=sns.displot(data=dffilter, x='City', y='Valuation ($B)', kind='kde'  )
g.figure.suptitle("sns.displot(data=dffilter, x='City', y='Valuation ($B)' , kind='kde'  )"  )

# Display the plot
g.figure.show()
read = input("Wait for me....")
#g.figure.clear()

#kind='kde'
g=sns.kdeplot(data=dffilter, x="City")
g.figure.suptitle("sns.kdeplot(data=dffilter, x=City)"  )

# Display the plot
g.figure.show()
read = input("Wait for me....")
#g.figure.clear()

g = sns.histplot(data=dffilter, x='City', y='Valuation ($B)', hue='Country', multiple="stack")
g.figure.suptitle("sns.histplot(data=dffilter, x='City', y='Valuation ($B)', hue='Country', multiple=stack)"  )
# Display the plot
g.figure.show()
read = input("Wait for me....")
#g.figure.clear()

# Use Seaborn to create a plot
g = sns.scatterplot(x='City', y='Valuation ($B)', data=dffilter)
g.figure.suptitle("sns.scatterplot(x='City', y='Valuation ($B)', data=dffilter)"  )
g.figure.show()
read = input("Wait for me....")
#g.figure.clear()

g=sns.lineplot(data=dffilter, x='City', y='Valuation ($B)' )
g.figure.suptitle("sns.lineplot(data=dffilter, x=City , y=Valuation ($B)  )"  )
# Display the plot
g.figure.show()
read = input("Wait for me....")
#g.figure.clear()

g=sns.barplot(data=dffilter, x="City", y="Valuation ($B)", legend=False)
g.figure.suptitle("sns.barplot(data=dffilter, x=City, y=Valuation ($B), legend=False)"  )
# Display the plot
g.figure.show()
read = input("Wait for me....")
#g.figure.clear()

g=sns.catplot(data=dffilter, x="City", y="Valuation ($B)")
g.figure.suptitle("sns.catplot(data=df, x=City, y=Valuation ($B))"  )
# Display the plot
g.figure.show() 
read = input("Wait for me....")
#g.figure.clear()

#.pivot(index="Model", columns="agency", values="price")
glue = dffilter.pivot(columns="City", values="Valuation ($B)")

g=sns.heatmap(glue)
g.figure.suptitle("sns.heatmap(glue)  - glue = dffilter.pivot(columns=City, values=Valuation ($B))"  )
# Display the plot
g.figure.show()
read = input("Wait for me....")
#g.figure.clear()
