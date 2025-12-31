#FastFoodRestaurants
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt 


df = pd.read_csv(r'Amna-AI-Course-Bin/PandasPractice/FastFoodRestaurants (1).csv',delimiter=",")

print(df)

print("df - data types" , df.dtypes)

print("df.info():   " , df.info() )

# display the last three rows
print('Last three Rows:')
print(df.tail(3))

# display the first three rows
print('First Three Rows:')
print(df.head(3))
print()

#Summary of Statistics of DataFrame using describe() method.
print("Summary of Statistics of DataFrame using describe() method", df.describe())

#Counting the rows and columns in DataFrame using shape(). It returns the no. of rows and columns enclosed in a tuple.
print("Counting the rows and columns in DataFrame using shape() : " ,df.shape)
print()



# access the Name column

country= df['country']
print("access the Name column: df : ")
print(country)
print()

"""
0            Real Biz International
1                       Khan Estate
2                   Shahum Estate 2
3                               NaN
4                               NaN
                   ...
144    Harum Real Estate & Builders
145                     Almo Estate
146              Gateway Properties
147             Chughtai Associates
148             Chughtai Associates
"""

# access multiple columns
country_name = df[['country','name']]
print("access multiple columns: df : ")
print(country_name)
print()


""""                           agency                    agent
0          Real Biz International               Usama Khan
1                     Khan Estate         mohsinkhan and B
2                 Shahum Estate 2  Babar Hameed, Raja Omar
3                             NaN                      NaN
4                             NaN                      NaN
..                            ...                      ...
144  Harum Real Estate & Builders                Rashid Ch
145                   Almo Estate              ALMO Estate
146            Gateway Properties           Muhammad Faraz
147           Chughtai Associates         Mehboob Chughtai
148           Chughtai Associates         Mehboob Chughtai"""




"""There are four primary ways to select rows with .loc. These include:
Selecting a single row
Selecting multiple rows
Selecting a slice of rows
Conditional row selection"""

# Case 1 : using .loc - default case - starts here
# Reference: https://www.datacamp.com/tutorial/loc-vs-iloc
# 
"""
Syntax               df.loc[row_indexer, column_indexer]              df.iloc[row_indexer, column_indexer]
Indexing Method      Label-based                                      Position-based indexing
Used for Reference   Row and column labels (names)                    Numerical indices of rows and columns (starting from 0)
"""
#Selecting a single row using .loc
second_row = df.loc[1]
print("#Selecting a single row using .loc")
print(second_row)
print()

#Selecting multiple rows using .loc
second_row2 = df.loc[[1, 3]]
print("#Selecting multiple rows using .loc")
print(second_row2)
print()

#Selecting a slice of rows using .loc
second_row3 = df.loc[1:5]
print("#Selecting a slice of rows using .loc")
print(second_row3)
print()
# loc works on primary key and iloc works on index like array

#Conditional selection of rows using .loc
second_row4 = df.loc[df['country'] == 'province']
print("#Conditional selection of rows using .loc")
print(second_row4)
print()

#Selecting a single column using .loc
second_row5 = df.loc[:1,'country']
print("#Selecting a single column using .loc")
print(second_row5)
print()

#Selecting multiple columns using .loc
second_row6 = df.loc[:1,['country','name']]
print("#Selecting multiple columns using .loc")
print(second_row6)
print()

#Selecting a slice of columns using .loc
second_row7 = df.loc[:1,'address':'keys']
print("#Selecting a slice of columns using .loc")
print(second_row7)
print()

#Combined row and column selection using .loc
second_row8 = df.loc[df['country'] == 'Gateway Properties','name':'website']
print("#Combined row and column selection using .loc")
print(second_row8)
print()
# Case 1 : using .loc - default case - ends here

# loc works on primary key iloc works on index column
print("# Case 2 : using .loc with index_col - starts here")
# Case 2 : using .loc with index_col - starts here
# Second cycle - with index_col as property_id
# Why Second cycle - Note Index - , index_col='property_id'
df_index_col = pd.read_csv(r'Amna-AI-Course-Bin/PandasPractice/FastFoodRestaurants (1).csv',delimiter="," , index_col='latitude')

print(df_index_col)
print(df_index_col.dtypes)
print(df_index_col.info())
# Second cycle - with index_col as property_id

#Selecting a single row using .loc
second_row = df_index_col.loc[44.9213]
print("#Selecting a single row using .loc")
print(second_row)
print()

#Selecting multiple rows using .loc
second_row2 = df_index_col.loc[[44.9213, 44.95008]]
print("#Selecting multiple rows using .loc")
print(second_row2)
print()

#Selecting a slice of rows using .loc
second_row3 = df_index_col.loc[39.86969:33.61937]
print("#Selecting a slice of rows using .loc")
print(second_row3)
print()

#Conditional selection of rows using .loc
second_row4 = df_index_col.loc[df_index_col['country'] == 'Gateway Properties']
print("#Conditional selection of rows using .loc")
print(second_row4)
print()

#Selecting a single column using .loc
second_row5 = df_index_col.loc[:35.52234,'country']
print("#Selecting a single column using .loc")
print(second_row5)
print()


#Selecting multiple columns using .loc
second_row6 = df_index_col.loc[:40.803141,['country','name']]
print("#Selecting multiple columns using .loc")
print(second_row6)
print()

#Selecting a slice of columns using .loc
second_row7 = df_index_col.loc[:33.450731,'location':'agency']
print("#Selecting a slice of columns using .loc")
print(second_row7)
print()

#Combined row and column selection using .loc   # columns whose names are gateway prop.
second_row8 = df_index_col.loc[df_index_col['keys'] == 'Gateway Properties','location':'keys']
print("#Combined row and column selection using .loc")
print(second_row8)
print()

# Case 2 : using .loc with index_col  -  ends here


print("# Case 3 : Using .iloc - starts here")
# Case 3 : Using .iloc - starts here
"""Using .iloc: Selection by Integer Position
.iloc selects by position instead of label. This is the standard syntax of using .iloc: df.iloc[row_indexer, column_indexer]. There are two special things to look out for:

Counting starting at 0: The first row and column have the index 0, the second one index 1, etc.
Exclusivity of range end value: When using a slice, the row or column specified behind the colon is not included in the selection."""

#Selecting a single row using .iloc
second_row = df_index_col.iloc[0]
print("#Selecting a single row using .iloc")
print(second_row)
print()

#Selecting multiple rows using .iloc
second_row2 = df_index_col.iloc[[1, 3,5]]
print("#Selecting multiple rows using .iloc")
print(second_row2)
print()

#Selecting a slice of rows using .iloc
second_row3 = df_index_col.iloc[2:5]
print("#Selecting a slice of rows using .iloc")
print(second_row3)
print()

#Selecting a single column using .iloc
second_row5 = df_index_col.iloc[:,2]
print("#Selecting a single column using .iloc")
print(second_row5)
print()

#Selecting multiple columns using .iloc
second_row6 = df_index_col.iloc[:,[2,4]]
print("#Selecting multiple columns using .iloc")
print(second_row6)
print()

#Selecting a slice of columns using .iloc
second_row7 = df_index_col.iloc[:,2:4]
print("#Selecting a slice of columns using .iloc")
print(second_row7)
print()

#Combined row and column selection using .iloc
second_row8 = df_index_col.iloc[[1, 3,5],2:4]
print("#Combined row and column selection using .iloc")
print(second_row8)
print()

# Case 3 : Using .iloc - ends here

# Next Run 
print("Next Run")

""""Pandas DataFrame Manipulation
DataFrame manipulation in Pandas involves editing and modifying existing DataFrames. Some common DataFrame manipulation operations are:

Adding rows/columns
Removing rows/columns
Renaming rows/columns"""

#Add a New Row to a Pandas DataFrame
# add a new row
# Copy array from list and add to DataFrame
# 3477952;82;"https://www.zameen.com/Property/lahore_model_town_6_kanal_excellent_house_for_sale_in_model_town-347795-8-12.html";"House2";2200000002;"Model Town2";"Lahore2";"Punjab2";312.483868658082;742.325685501099;02;"6 Kanal2";"For Sale2";02;"07-17-2019";"Real Biz International2";"Usama Khan2"

#df.loc[len(df.index)]=[530 Clinton Ave,Washington Court House,US,us/oh/washingtoncourthouse/53/-791445730,39.53255,-83.44526,Wendy's,43160,OH,http://www.wendys.com ]
print("Modified DataFrame - add a new row:")
print(df)
print()

#Remove Rows/Columns from a Pandas DataFrame


# delete row with index 1  # Axis 0 determine row and drop row 1
df.drop(1, axis=0, inplace=True)
# delete row with index 1
df.drop(index=2, inplace=True)
# delete rows with index 3 and 5
df.drop([3, 5], axis=0, inplace=True)
# display the modified DataFrame after deleting rows
print("Modified DataFrame - Remove Rows:")
print(df)



# delete age column # Axis 1 means column
df.drop('longitude', axis=1, inplace=True) # inplace means to drop from given df otherwise we should store modified df after inplaced df in other variable
# delete marital status column
df.drop(columns='keys', inplace=True)
# delete height and profession columns
df.drop(['websites', 'city'], axis=1, inplace=True)
# display the modified DataFrame after deleting rows
print("Modified DataFrame -  delete page_url ,property_type , location , city , column :")
print(df)


#Rename Labels in a DataFrame
# rename column 'Name' to 'First_Name'
df.rename(columns= {'province_name': 'province_nameChanged'}, inplace=True)
# rename columns 'Age' and 'City'
df.rename(mapper= {'bedrooms': 'bedrooms_Changed', 'date_added':'date_added_Changed'}, axis=1, inplace=True)
# display the DataFrame after renaming column
print("Modified DataFrame  - Rename Labels :")
print(df)


#Example: Rename Row Labels
# rename column one index label
df.rename(index={0: 7}, inplace=True)
# rename columns multiple index labels
df.rename(mapper={1: 10, 2: 100}, axis=0, inplace=True)
# display the DataFrame after renaming column
print("Modified DataFrame - Rename Row - 0  >>> 7 , 1 >>> 10 , 2 >>> 100  Labels:")
print(df)



#query() to Select Data
#The query() method in Pandas allows you to select data using a more SQL-like syntax.

# select the rows where the age is greater than 25
selected_rows = df.query('latitude == \'Gateway Properties\' or latitude > 39.35155')

print(selected_rows.to_string())
print(len(selected_rows))



# sort DataFrame by price in ascending order
sorted_df = df.sort_values(by='latitude')
print(sorted_df.to_string(index=False))

#Sort Pandas DataFrame by Multiple Columns

# 1. Sort DataFrame by 'Age' and then by 'Score' (Both in ascending order)
df1 = df.sort_values(by=['latitude', 'name'])

print("Sorting by 'price' (ascending) and then by 'location_id' (ascending):\n")
print(df1.to_string(index=False))


"""
Reference: https://www.geeksforgeeks.org/python-pandas-dataframe-to_string/
Explanation: This code creates a DataFrame from a dictionary with three columns (Weight, Name, Age), structures it into a tabular format using pd.DataFrame() and converts it into a fully visible string representation with df.to_string().

Syntax
DataFrame.to_string(buf=None, columns=None, col_space=None, header=True, index=True, na_rep=’NaN’, formatters=None, float_format=None, sparsify=None, index_names=True, justify=None, max_rows=None, max_cols=None, show_dimensions=False, decimal=’.’, line_width=None)


Parameters:

buf: Buffer to write the output string to (e.g., a file). Defaults to None, which means the output is returned as a string.
columns: Specifies a subset of columns to include in the output. If None, all columns are printed.
col_space: Defines the minimum width of each column.
header: Whether to print column names. Can also accept a list of column name aliases.
index: Whether to include index labels. Default is True.
na_rep: String representation for missing values (NaN). Default is ‘NaN’.
formatters: Dictionary or list of functions to apply to columns for formatting their output.
float_format: Formatter function to apply specifically to floating-point numbers.
sparsify: Controls hierarchical index formatting. If False, prints every multi-index key at each row.
index_names: Whether to print index names. Default is True.
justify: Alignment of column headers (‘left’, ‘right’, ‘center’, ‘justify’ or ‘justify-all’).
max_rows: Maximum number of rows to display. If exceeded, truncates output.
max_cols: Maximum number of columns to display. If exceeded, truncates output.
show_dimensions: If True, displays the shape (rows x columns) of the DataFrame.
decimal: Specifies the character for decimal separation (e.g., ‘,’ for European formatting).
line_width: Defines the maximum character width of a row before wrapping text."""



#Pandas groupby
#In Pandas, the groupby operation lets us group data based on specific columns. This means we can divide a DataFrame into smaller groups based on the values in these columns.

# group the DataFrame by the location_id column and
# calculate the sum of price for each category
grouped = df.groupby('latitude')['latitude'].sum()

print(grouped.to_string())
print("grouped :" , len(grouped))


""""Pandas Data Cleaning
Data cleaning means fixing and organizing messy data. Pandas offers a wide range of tools and functions to help us clean and preprocess our data effectively.
"""
# use dropna() to remove rows with any missing values
df_cleaned = df.dropna()
print("Cleaned Data:\n",df_cleaned)


# filling NaN values with 0
df.fillna(0, inplace=True)

print("\nData after filling NaN with 0:\n", df)



# create a list named data
data = [2, 4, 6, 8]
# create Pandas array using data
array1 = pd.array(data)
print(array1)
"""<IntegerArray>
[2, 4, 6, 8]
Length: 4, dtype: Int64"""


# creating a pandas.array of integers
int_array = pd.array([1, 2, 3, 4, 5], dtype='int')
print(int_array)
print()

#Pandas Reshape
#In Pandas, reshaping data refers to the process of converting a DataFrame from one format to another for better data visualization and analysis.
#Pandas provides multiple methods like pivot(), pivot_table(), stack(), unstack() and melt() to reshape data. We can choose the method based on our analysis requirement.


# to be continued....



#############Seaborn Part
 


#https://seaborn.pydata.org/generated/seaborn.set_theme.html
#https://seaborn.pydata.org/tutorial/aesthetics.html
#https://python-charts.com/seaborn/themes/
"""
 Built-in Themes
Seaborn provides five built-in themes:
darkgrid: Adds a gray background with white gridlines. It is the default theme.
whitegrid: Adds gray gridlines on a white background.
dark: Similar to darkgrid but without the gridlines.
white: Similar to whitegrid but without the gridlines.
ticks: Adds ticks to the axes and uses a white background.
Setting Themes
The seaborn.set_theme() or seaborn.set_style() function can be used to set the theme for all plots. """

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


"""Customizing Themes
It is possible to customize the themes further by passing a dictionary of parameters to the rc argument of seaborn.set_theme() or seaborn.set_style(). This allows for fine-grained control over the appearance of plots."""

# Customize the  theme # we can overwrite things using rc dictionary
sns.set_theme(style='darkgrid', rc={'axes.facecolor': 'grey', 'grid.color': 'white'})

# Create a plot
sns.lineplot(x='province', y='latitude', data=data)
plt.show()

"""seaborn.set_theme() allows customization of the appearance of plots by modifying matplotlib's rc parameters. It accepts a dictionary rc to override default settings. Here's a breakdown of commonly used rc parameters:
axes.facecolor: Background color of the plotting area (e.g., 'white', '#EAEAF2').
axes.edgecolor: Color of the axes lines (e.g., 'black', 'gray').
axes.linewidth: Width of the axes lines in points.
axes.grid: Whether to show the grid ('True' or 'False').
axes.grid.axis: Which axes to show the grid lines on ('x', 'y', or 'both').
axes.grid.which: Which grid lines to draw ('major', 'minor', or 'both').
axes.labelcolor: Color of the axis labels.
axes.labelsize: Size of the axis labels in points or as a relative string (e.g., 'large', 'small').
axes.titlesize: Size of the plot title.
xtick.color: Color of the x-axis tick marks and labels.
ytick.color: Color of the y-axis tick marks and labels.
xtick.labelsize: Size of the x-axis tick labels.
ytick.labelsize: Size of the y-axis tick labels.
grid.color: Color of the grid lines.
grid.linewidth: Width of the grid lines.
font.family: Font family to use (e.g., 'sans-serif', 'serif', 'monospace').
font.size: Default font size for text elements.
lines.linewidth: Width of lines in plots.
lines.linestyle: Style of lines (e.g., '-', '--', '-.', ':').
patch.edgecolor: Color of patch edges (e.g., in histograms, bar plots).
patch.linewidth: Width of patch edges.
legend.frameon: Whether to display a frame around the legend ('True' or 'False').
legend.fontsize: Size of the legend text.
figure.figsize: Size of the figure (width, height) in inches.
figure.facecolor: Background color of the entire figure."""

#Zameencom data - based examples
# Load data from a CSV file
df = pd.read_csv(r'Amna-AI-Course-Bin/NumpyPractice/FastFoodRestaurants (1).csv',delimiter=",", index_col='latitude')

print(df.dtypes)
dffilter= df.head(40)
dffilter100= df.head(100)
# https://seaborn.pydata.org/api.html#distribution-api

"""Distribution plots
displot    -  Figure-level interface for drawing distribution plots onto a FacetGrid.

histplot   -  Plot univariate or bivariate histograms to show distributions of datasets.

kdeplot    -  Plot univariate or bivariate distributions using kernel density estimation.

ecdfplot   -  Plot empirical cumulative distribution functions.

rugplot    -  Plot marginal distributions by drawing ticks along the x and y axes."""


#https://seaborn.pydata.org/generated/seaborn.set_theme.html
#https://seaborn.pydata.org/tutorial/aesthetics.html
#https://seaborn.pydata.org/tutorial/color_palettes.html

sns.set(style="whitegrid")


#https://seaborn.pydata.org/generated/seaborn.displot.html#seaborn.displot
"""This function provides access to several approaches for visualizing the univariate or bivariate distribution of data, including subsets of data defined by semantic mapping and faceting across multiple subplots. The kind parameter selects the approach to use:

histplot() (with kind="hist"; the default)

kdeplot() (with kind="kde")

ecdfplot() (with kind="ecdf"; univariate-only)"""

#kind='hist'  
g=sns.displot(data=dffilter, x="province" , y="latitude" , hue="city",  kind='hist'  )
g.figure.suptitle("sns.displot(data=dffilter, x=agency , y=price , hue=agent,  kind='hist'  )"  )

# Display the plot
g.figure.show()
read = input("Wait for me....")
#g.figure.clear()


""""kind="kde" in Seaborn specifies the use of Kernel Density Estimation plots. KDE plots visualize the probability density of a continuous variable. Instead of discrete bins like in histograms, KDE plots use a continuous curve to estimate the underlying distribution of the data. This provides a smoother and often more informative representation of the data's distribution, especially for continuous variables."""
#kind='kde'
g=sns.displot(data=dffilter, x="city" , y="latitude" , kind='kde'  )
g.figure.suptitle("sns.displot(data=dffilter, x=price , y=date_added , kind='kde'  )"  )

# Display the plot
g.figure.show()
read = input("Wait for me....")
#g.figure.clear()

#https://seaborn.pydata.org/generated/seaborn.kdeplot.html
#kind='kde'
g=sns.kdeplot(data=dffilter, x="city")
g.figure.suptitle("sns.kdeplot(data=dffilter, x=price)"  )

# Display the plot
g.figure.show()
read = input("Wait for me....")
#g.figure.clear()


# See: https://seaborn.pydata.org/generated/seaborn.histplot.html#seaborn.histplot
"""Plot univariate or bivariate histograms to show distributions of datasets.
A histogram is a classic visualization tool that represents the distribution of one or more variables by counting the number of observations that fall within discrete bins."""
g = sns.histplot(data=dffilter, x='city', y='latitude', hue='longitude', multiple="stack")
g.figure.suptitle("sns.histplot(data=dffilter, x='agency', y='price', hue='agency', multiple=stack)"  )
# Display the plot
g.figure.show()
read = input("Wait for me....")
#g.figure.clear()

#https://seaborn.pydata.org/generated/seaborn.scatterplot.html#seaborn.scatterplot
"""Draw a scatter plot with possibility of several semantic groupings.

The relationship between x and y can be shown for different subsets of the data using the hue, size, and style parameters. These parameters control what visual semantics are used to identify the different subsets. It is possible to show up to three dimensions independently by using all three semantic types, but this style of plot can be hard to interpret and is often ineffective. Using redundant semantics (i.e. both hue and style for the same variable) can be helpful for making graphics more accessible."""
# Use Seaborn to create a plot
g = sns.scatterplot(x='city', y='latitude', data=dffilter)
g.figure.suptitle("sns.scatterplot(x='agency', y='price', data=dffilter)"  )
g.figure.show()
read = input("Wait for me....")
#g.figure.clear()


#https://seaborn.pydata.org/generated/seaborn.lineplot.html
"""Draw a line plot with possibility of several semantic groupings.

The relationship between x and y can be shown for different subsets of the data using the hue, size, and style parameters. These parameters control what visual semantics are used to identify the different subsets. It is possible to show up to three dimensions independently by using all three semantic types, but this style of plot can be hard to interpret and is often ineffective. Using redundant semantics (i.e. both hue and style for the same variable) can be helpful for making graphics more accessible."""
g=sns.lineplot(data=dffilter, x="city" , y="latitude"  )
g.figure.suptitle("sns.lineplot(data=dffilter, x=agency , y=price  )"  )
# Display the plot
g.figure.show()
read = input("Wait for me....")
#g.figure.clear()



#https://seaborn.pydata.org/generated/seaborn.barplot.html
"""Show point estimates and errors as rectangular bars.

A bar plot represents an aggregate or statistical estimate for a numeric variable with the height of each rectangle and indicates the uncertainty around that estimate using an error bar. Bar plots include 0 in the axis range, and they are a good choice when 0 is a meaningful value for the variable to take."""
g=sns.barplot(data=dffilter, x="city", y="latitude", legend=False)
g.figure.suptitle("sns.barplot(data=dffilter, x=agency, y=price, legend=False)"  )
# Display the plot
g.figure.show()
read = input("Wait for me....")
#g.figure.clear()


#https://seaborn.pydata.org/generated/seaborn.catplot.html
""""Figure-level interface for drawing categorical plots onto a FacetGrid.

This function provides access to several axes-level functions that show the relationship between a numerical and one or more categorical variables using one of several visual representations. The kind parameter selects the underlying axes-level function to use."""

g=sns.catplot(data=dffilter, x="city", y="latitude")
g.figure.suptitle("sns.catplot(data=df, x=agency, y=price)"  )
# Display the plot
g.figure.show() 
read = input("Wait for me....")
#g.figure.clear()




#https://seaborn.pydata.org/generated/seaborn.heatmap.html
""""Plot rectangular data as a color-encoded matrix.

This is an Axes-level function and will draw the heatmap into the currently-active Axes if none is provided to the ax argument. Part of this Axes space will be taken and used to plot a colormap, unless cbar is False or a separate Axes is provided to cbar_ax."""
#.pivot(index="Model", columns="agency", values="price")
glue = dffilter.pivot(columns="latitude", values="city")

g=sns.heatmap(glue)
g.figure.suptitle("sns.heatmap(glue)  - glue = dffilter.pivot(columns=agency, values=price)"  )
# Display the plot
g.figure.show()
read = input("Wait for me....")
#g.figure.clear()