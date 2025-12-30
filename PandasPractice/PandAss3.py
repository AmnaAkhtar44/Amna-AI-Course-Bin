# Startups in 2021

import pandas as pd
df =pd.read_csv(r'Amna-AI-Course-Bin/PandasPractice/Startups in 2021 end.csv' , delimiter = "," ,  dayfirst=True , date_format={'date_added': '%d-%m-%Y'})
print(df)

#Datatypes
print("Print df.data types here:" , df.dtypes)
#Info
print("Print df.info here:" , df.info())
#Tail
print("Print last 3 rows here" , df.tail(3))
#Head
print("Print First 3 Rows here:" , df.head(3))
#Describe
print("Print df.describe to describe all stats operations:" , df.describe())
#Shape
print("Print df.shape here" , df.shape)

##Valuation
df['Valuation ($B)'] = df['Valuation ($B)'].str.replace('$','')
print(df['Valuation ($B)'])
print(df)
df['Valuation ($B)'] = df['Valuation ($B)'].astype(float)
print(df.dtypes)
df['Date Joined'] = pd.to_datetime(df['Date Joined'])
Date_Joined = df['Date Joined']
print("Access the column df")
print(Date_Joined)



# access the Name column
City = df['City']
print("Access the name column here" ) 
print(City)
print()


# access multiple columns
Country_City = df[['Country' , 'City']]
print("Access the multiple columns here:")
print(Country_City)
print(df)

Company_Valuation = df[['Company','Valuation ($B)']]
print("access multiple columns: df : ")
print(Company_Valuation)
print()



# Case 1 : using .loc - default case - starts here
# Reference: https://www.datacamp.com/tutorial/loc-vs-iloc
# 
"""
Syntax               df.loc[row_indexer, column_indexer]              df.iloc[row_indexer, column_indexer]
Indexing Method      Label-based                                      Position-based indexing
Used for Reference   Row and column labels (names)                    Numerical indices of rows and columns (starting from 0)
"""
#Selecting a single row using .loc
second_row1 = df.loc[15]
print("Access this row using loc")
print(second_row1)
print()

#Selecting multiple rows using .loc
second_row2 = df.loc[[15,16]]
print("Access multiple rows using loc")
print(second_row2)
print()

#Selecting a slice of rows using .loc
second_row3 = df.loc[10:15]
print("Acces slice of Rows using loc")
print(second_row3)
print()
# loc works on primary key and iloc works on index like array

#Conditional selection of rows using .loc
second_row4 = df.loc[df['Company'] == 'Gateway Properties']
print("Print conditional selectional using loc here")
print(second_row4)
print()
#Selecting a single column using .loc
second_row5= df.loc[:2 , 'Company']
print("Acces the column df here")
print(second_row5)
print(df)

#Selecting multiple columns using .loc
second_row6 = df.loc[:2 , ['City' , 'Country']]
print("Access these columns df here:")
print(second_row6)
print(df)

#Selecting a slice of columns using .loc
second_row7 = df.loc[:3 , 'Country' : 'Industry']
print("Print Slicing of columns df here:")
print(second_row7)
print(df)

#Combined row and column selection using .loc
second_row8 = df.loc[df['Company'] == 'SpaceX','Valuation ($B)':'Select Investors']
print("#Combined row and column selection using .loc")
print(second_row8)
print()
# Case 1 : using .loc - default case - ends here
print("# Case 2 : using .loc with index_col - starts here")

# loc works on primary key iloc works on index column
# Case 2 : using .loc with index_col - starts here
# Second cycle - with index_col as property_id
# Why Second cycle - Note Index - , index_col='property_id
df_index_col = pd.read_csv('Amna-AI-Course-Bin/PandasPractice/Startups in 2021 end.csv',delimiter=";",parse_dates=[14], date_format={'date_added': '%d-%m-%Y'} , index_col='SpaceX')
print(df_index_col)
print(df_index_col.dtypes)
print(df_index_col.info())


#Selecting a single row using .loc
second_row = df_index_col.loc[200]
print("Access single row")
print(second_row)
print(df)
#Selecting multiple rows using .loc


#Selecting a slice of rows using .loc

#Conditional selection of rows using .loc

#Selecting a single column using .loc



#Selecting multiple columns using .loc


#Selecting a slice of columns using .loc

#Combined row and column selection using .loc   # columns whose names are gateway prop.

# Case 2 : using .loc with index_col  -  ends here


print("# Case 3 : Using .iloc - starts here")
# Case 3 : Using .iloc - starts here
"""Using .iloc: Selection by Integer Position
.iloc selects by position instead of label. This is the standard syntax of using .iloc: df.iloc[row_indexer, column_indexer]. There are two special things to look out for:

Counting starting at 0: The first row and column have the index 0, the second one index 1, etc.
Exclusivity of range end value: When using a slice, the row or column specified behind the colon is not included in the selection."""

#Selecting a single row using .iloc


#Selecting multiple rows using .iloc


#Selecting a slice of rows using .iloc


#Selecting a single column using .iloc


#Selecting multiple columns using .iloc

#Combined row and column selection using .iloc


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

#df.loc[len(df.index)] = 


#Remove Rows/Columns from a Pandas DataFrame


# delete row with index 1  # Axis 0 determine row and drop row 1
# delete row with index 1
# delete rows with index 3 and 5
# display the modified DataFrame after deleting rows



# delete age column # Axis 1 means column
 # inplace means to drop from given df otherwise we should store modified df after inplaced df in other variable
# delete marital status column
# delete height and profession columns
# display the modified DataFrame after deleting rows



#Rename Labels in a DataFrame
# rename column 'Name' to 'First_Name'
# rename columns 'Age' and 'City'
# display the DataFrame after renaming column


#Example: Rename Row Labels
# rename column one index label
# rename columns multiple index labels
# display the DataFrame after renaming column



#query() to Select Data
#The query() method in Pandas allows you to select data using a more SQL-like syntax.

# select the rows where the age is greater than 25




# sort DataFrame by price in ascending order

#Sort Pandas DataFrame by Multiple Columns

# 1. Sort DataFrame by 'Age' and then by 'Score' (Both in ascending order)



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



""""Pandas Data Cleaning
Data cleaning means fixing and organizing messy data. Pandas offers a wide range of tools and functions to help us clean and preprocess our data effectively.
"""
# use dropna() to remove rows with any missing values


# filling NaN values with 0




# create a list named data
# create Pandas array using data
"""<IntegerArray>
[2, 4, 6, 8]
Length: 4, dtype: Int64"""


# creating a pandas.array of integers

#Pandas Reshape
#In Pandas, reshaping data refers to the process of converting a DataFrame from one format to another for better data visualization and analysis.
#Pandas provides multiple methods like pivot(), pivot_table(), stack(), unstack() and melt() to reshape data. We can choose the method based on our analysis requirement.


# to be continued....