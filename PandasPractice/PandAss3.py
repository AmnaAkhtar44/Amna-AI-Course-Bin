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
df_index_col = pd.read_csv('Amna-AI-Course-Bin/PandasPractice/Startups in 2021 end.csv',delimiter=",",parse_dates=['Date Joined'] ,index_col=0)#parse_dates=[14], date_format={'date_added': '%d-%m-%Y'} , index_col=0)
print(df_index_col)
print(df_index_col.head())
print(df_index_col.dtypes)
print(df_index_col.info())


#Selecting a single row using .loc
second_row = df_index_col.loc[200]
print("Access single row")
print(second_row)
print(df)

#Selecting multiple rows using .loc
second_row1 = df_index_col.loc[[451 , 551]]
print("Access multiple Rows")
print(second_row1)
print(df)

#Selecting a slice of rows using .loc
second_row2 = df_index_col.loc[250:700]
print("Access slice of columns")
print(second_row2)
print(df)

#Conditional selection of rows using .loc
second_row4 = df_index_col.loc[df_index_col['Company'] == 'Gateway Properties']
print("#Conditional selection of rows using .loc")
print(second_row4)
print()

#Selecting a single column using .loc
second_row5 = df_index_col.loc[:550,'City']
print("#Selecting a single column using .loc")
print(second_row5)
print()


#Selecting multiple columns using .loc
second_row6 = df_index_col.loc[:550,['Country','City']]
print("#Selecting multiple columns using .loc")
print(second_row6)
print()

#Selecting a slice of columns using .loc
second_row7 = df_index_col.loc[:550,'Country' : 'Industry']
print("#Selecting multiple columns using .loc")
print(second_row7)
print()

#Combined row and column selection using .loc   # columns whose names are gateway prop.
second_row8 = df_index_col.loc[df_index_col['Company'] == 'Gateway Properties','Country':'Industry']
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

#df.loc[len(df.index)] = [157,Impossible Foods,$4,5/13/2019,United States,Redwood City,Consumer & retail,"Khosla Ventures, Horizons Ventures,Temasek Holdings"]
print("Modified DataFrame - add a new row:")
print(df)
print()



#Remove Rows/Columns from a Pandas DataFrame


df.drop(1, axis=0, inplace=True)
# delete row with index 1
df.drop(index=2, inplace=True)
# delete rows with index 3 and 5
df.drop([3, 5], axis=0, inplace=True)
# display the modified DataFrame after deleting rows
print("Modified DataFrame - Remove Rows:")
print(df)



# delete age column # Axis 1 means column
df.drop('Company', axis=1, inplace=True) # inplace means to drop from given df otherwise we should store modified df after inplaced df in other variable
# delete marital status column
df.drop(columns='City', inplace=True)
# delete height and profession columns
df.drop(['Country', 'Industry'], axis=1, inplace=True)
# display the modified DataFrame after deleting rows
print("Modified DataFrame -  delete page_url ,property_type , location , city , column :")
print(df)

#Rename Labels in a DataFrame
# rename column 'Name' to 'First_Name'
df.rename(columns= {'Company': 'Company_nameChanged'}, inplace=True)
# rename columns 'Age' and 'City'
df.rename(mapper= {'City': 'City_Changed', 'date_added':'date_added_Changed'}, axis=1, inplace=True)
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

#selected_rows = df.query('Valuation ($B) == \'Gateway Properties\' or Valuation ($B) > $25')

#print(selected_rows.to_string())
#print(len(selected_rows))



# sort DataFrame by price in ascending order

#Sort Pandas DataFrame by Multiple Columns

# 1. Sort DataFrame by 'Age' and then by 'Score' (Both in ascending order)
#df1 = df.sort_values(by=['City', 'Industry'])

print("Sorting by 'price' (ascending) and then by 'location_id' (ascending):\n")
#print(df1.to_string(index=False))

#grouped = df.groupby('City')['Industry'].sum()

#print(grouped.to_string())
#print("grouped :" , len(grouped))


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



