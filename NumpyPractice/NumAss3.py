# US-Startups Funding in 2021 end.csv
import numpy as np

ID , company , valuation = np.genfromtxt(r'Amna-AI-Course-Bin\NumpyPractice\Startups in 2021 end.csv', delimiter=',', usecols=(0,1,2), unpack=True, dtype=None, skip_header=1, invalid_raise=False)


valuation = np.char.replace(valuation, "$", "")
valuation = valuation.astype(float)

print(company)
print(valuation)
print(ID)

# US Startups Funding- valuation - Statistical Operations 



print("US Startups Fundings valuation mean: ",np.mean(valuation))
print("US Startups Fundings valuation mod: ",np.median(valuation))
print("US Startups Fundings valuation average: ",np.average(valuation))
print("US Startups Fundings valuation std: ",np.std(valuation))
print("US Startups Fundings valuation min: ",np.min(valuation))
print("US Startups Fundings valuation max: ",np.max(valuation))
print("US Startups Fundings valuation - percentile - 25: ",np.percentile(valuation,25))
print("US Startups Fundings valuation - percentile - 75:",np.percentile(valuation,75))
print("US Startups Fundings valuation - percentile - 3: ",np.percentile(valuation,3))

#  US Startups Fundings valuation - maths operations
print("US Startups Fundings valuation square: " , np.square(valuation))
print("US Startups Fundings valuation sqrt: " , np.sqrt(valuation))
print("US Startups Fundings valuation pow: " , np.power(valuation,valuation))
print("US Startups Fundings valuation abs: " , np.abs(valuation))

# Perform basic arithmetic operations
addition = ID + valuation
subtraction = ID - valuation
multiplication = ID * valuation
division = ID / valuation

print("US Startups Fundings valuation - Addition:", addition)
print("US Startups Fundings valuation - Subtraction:", subtraction)
print("US Startups Fundings valuation - Multiplication:", multiplication)
print("US Startups Fundings valuation - Division:", division)

#Trigonometric Functions

ValuationPie = (valuation/np.pi) +1
# Calculate sine, cosine, and tangent
sine_values = np.sin(ValuationPie)
cosine_values = np.cos(ValuationPie)
tangent_values = np.tan(ValuationPie)

print("US Startups Fundings valuation - div - pie  - Sine values:", sine_values)
print("US Startups Fundings valuation - pie Cosine values:", cosine_values)
print("US Startups Fundings valuation - div - pie Tangent values:", tangent_values)

print("US Startups Fundings valuation- div - pie  - Exponential values:", np.exp(ValuationPie))

# Calculate the natural logarithm and base-10 logarithm
log_array = np.log(ValuationPie)
log10_array = np.log10(ValuationPie)

print("US Startups Fundings valuation - div - pie  - Natural logarithm values:", log_array)
print("US Startups Fundings valuation - div - pie  = Base-10 logarithm values:", log10_array)

#Example: Hyperbolic Sine
# Calculate the hyperbolic sine of each element
sinh_values = np.sinh(ValuationPie)
print("US Startups Fundings valuation - div - pie   - Hyperbolic Sine values:", sinh_values)

#Hyperbolic Cosine Using cosh() Function
# Calculate the hyperbolic cosine of each element
cosh_values = np.cosh(ValuationPie)
print("US Startups Fundings valuation - div - pie   - Hyperbolic Cosine values:", cosh_values)

#Example: Hyperbolic Tangent
# Calculate the hyperbolic tangent of each element
tanh_values = np.tanh(ValuationPie)
print("US Startups Fundings valuation - div - pie   -Hyperbolic Tangent values:", tanh_values)

# Calculate the inverse hyperbolic sine of each element
asinh_values = np.arcsinh(ValuationPie)
print("US Startups Fundings valuation - pie   -Inverse Hyperbolic Sine values:", asinh_values)

#Example: Inverse Hyperbolic Cosine
# Calculate the inverse hyperbolic cosine of each element
acosh_values = np.arccosh(ValuationPie)
print("US Startups Fundings valuation - div - pie   -Inverse Hyperbolic Cosine values:", acosh_values)

# US Startups Fundings ID Plus Valuation - 2 dimentional arrary
D2IdVal = np.array([ID,
                     valuation])

print ("US Startups Fundings ID Plus valuation - 2 dimentional arrary - " ,D2IdVal)

# check the dimension of array1
print("US Startups Fundings ID Plus valuation - 2 dimentional arrary - dimension" , D2IdVal.ndim) 
# Output: 2

# return total number of elements in array1
print("US Startups Fundings ID Plus valuation - 2 dimentional arrary - total number of elements" ,D2IdVal.size)
# Output: size: 1872 

# return a tuple that gives size of array in each dimension
print("US Startups Fundings ID Plus valuation - 2 dimentional arrary - gives size of array in each dimension" ,D2IdVal.shape)
# Output: (2,936)

# check the data type of array1
print("US Startups Fundings ID Plus valuation - 2 dimentional arrary - data type" ,D2IdVal.dtype) 
# Output: float64

# Splicing array
D2IdValSlice=  D2IdVal[:1,:5]
print("US Startups Fundings ID Plus valuation - 2 dimentional arrary - Splicing array - D2IdVal[:1,:5] " , D2IdValSlice)
D2IdValSlice2=  D2IdVal[:1, 4:15:4]
print("US Startups Fundings ID Plus valuation - 2 dimentional arrary - Splicing array - D2IdVal[:1, 4:15:4] " , D2IdValSlice2)


# Indexing array
D2IdValSliceItemOnly=  D2IdValSlice[0,1]
print("US Startups Fundings ID Plus valuation - 2 dimentional arrary - Index array - D2IdValSlice[1,5] " , D2IdValSliceItemOnly)
D2IdValSlice2ItemOnly=  D2IdValSlice2[0, 2]
print("US Startups Fundings ID Plus valuation - 2 dimentional arrary - index array - D2IdValSlice2[0, 2] " , D2IdValSlice2ItemOnly)


#You should use the builtin function nditer, if you don't need to have the indexes values.
for elem in np.nditer(D2IdVal):
    print(elem)

#EDIT: If you need indexes (as a tuple for 2D table), then:
for index, elem in np.ndenumerate(D2IdVal):
    print(index, elem)


# 2 x 936 ========>>>>> 1  x 1872 - reshape
D2IdVal1TO1872 = np.reshape(D2IdVal, (1, 1872))
print("US Startups Fundings ID Plus valuation - 2 dimentional arrary - np.reshape(D2IdVal), (1, 1872)) : " , D2IdVal1TO1872)
print("US Startups Fundings ID Plus valuation - 2 dimentional arrary - np.reshape(D2IdVal), (1, 1872)) : Size " , D2IdVal1TO1872.size)
print("US Startups Fundings ID Plus valuation - 2 dimentional arrary - np.reshape(D2IdVal), (1, 1872)) : ndim " , D2IdVal1TO1872.ndim)
print("US Startups Fundings ID Plus valuation - 2 dimentional arrary - np.reshape(D2IdVal), (1, 1872)) : shape " , D2IdVal1TO1872.shape)
print("US Startups Fundings ID Plus valuation - 2 dimentional arrary - np.reshape(D2IdVal), (1, 1872)) : ndim " , D2IdVal1TO1872.ndim)




print()