# RealEstate-USA.csv
import numpy as np 

price, bed, bath, acre_lot, house_size = np.genfromtxt('Amna-AI-Course-Bin/NumpyPractice/RealEstate-USA (1).csv', delimiter=',', usecols=(2,3,4,5,9), unpack=True, dtype=None, skip_header=1, invalid_raise=False)

print(price)
print(bed)
print(bath)
print(acre_lot)
print(house_size)

# US Real Estate - price - Statistical Operations 
print("US Real Estate Price mean: ",np.mean(price))
print("US Real Estate Price mod: ",np.median(price))
print("US Real Estate Price average: ",np.average(price))
print("US Real Estate Price std: ",np.std(price))
print("US Real Estate Price min: ",np.min(price))
print("US Real Estate Price max: ",np.max(price))
print("US Real Estate Price - percentile - 25: ",np.percentile(price,25))
print("US Real Estate Price - percentile - 75:",np.percentile(price,75))
print("US Real Estate Price - percentile - 3: ",np.percentile(price,3))


# US Real Estate - Price - Maths Operations 
print("US Real Estate Price square: ",np.square(price))
print("US Real Estate Price sqrt: ",np.sqrt(price))
print("US Real Estate Price pow: ",np.power(price,price))
print("US Real Estate Price abs: ",np.abs(price))

# US Real Estate - Perform basic Arithmetic Operations 

addition = price + house_size
subtraction = price - house_size
multiplication = price * house_size
division = price / house_size

print("US Real Estate Price and House_Size - Addition", addition)
print("US Real Estate Price and House_Size - Subtraction", subtraction)
print("US Real Estate Price and House_Size - Multiplication", multiplication)
print("US Real Estate Price and House_Size - Division", division)

# Trigonomatric Functions 

pricepie = (price/np.pi) + 1

# Calculate Sine, Cosine, Tangent 

sine_values = np.sin(pricepie)
cosine_values = np.cos(pricepie)
tangent_values = np.tan(pricepie)

print("US Real Estate Price - div - pie - sine_values", sine_values)
print("US Real Estate Price - div - pie - cosine_values", cosine_values)
print("US Real Estate Price - div - pie - tangent_values", tangent_values)

print("US Real Estate Price - div - pie - Exponential values", np.exp(pricepie))

# Calculate natural logarithm and base-10 lorgarthm 

log_array = np.log(pricepie)
log10_array = np.log10(pricepie)

print("US Real Estate Price - div - pie - natural log", log_array)
print("US Real Estate Price - div - pie - base_10 log", log10_array)

# Example - Hyperbolic sine 
# Calculate the hyperbolic sine of each element 

sinh_values = np.sinh(pricepie)
print("US Real Estate Price - div - pie - hyperbolic sine values", sinh_values)

# Hyperbolic cosine using cosh() Function 
# Calculate the hyperbolic function of each element 

cosh_values = np.cosh(pricepie)
print("US Real Estate Price - div - pie - hyperbolic cos values", cosh_values)

# Example: Hyperbolic Tangent 
# Calculate the hyperbolic function of each element 

tanh_values = np.tanh(pricepie)
print("US Real Estate Price - div - pie - hyperbolic tan values", tanh_values)

# Example: Inverse hyperbolic sine 
# Calculate inverse hyperbolic sine of each element 

asinh_values = np.arcsin(pricepie)
print("US Real Estate Price - div - pie - inverse hyperbolic sine values", asinh_values)

# Example: Inverse hyperbolic cosine 
# Calculate the inverse hyperbolic cosine of each element 

acosh_values = np.arccosh(pricepie)
print("US Real Estate Price - div - pie - inverse hyperbolic cosine values", acosh_values)

# US Real Estate - bed plus bath 2 Dimensional Array 
D2BedBath = np.array([bed,
                       bath])

print("US Real Estate Price - bed plus bath - 2 Dimensional Array", D2BedBath)

# Check the Dimension of Array1
print("US Real Estate Price - bed plus bath - 2 Dimensional Array - Dimention", D2BedBath.ndim)

# return total number of elements in array 
print("US Real Estate Price - bed plus bath - 2 Dimensional Array - Size", D2BedBath.size)
# output 400 

# return a tuple that gives size of array in each dimension
print("US Real Estate Price - bed plus bath - 2 Dimensional Array - Shape", D2BedBath.shape)
# output (2,400)

# check the data type of array1
print("US Real Estate Price - bed plus bath - Array1 - datatype", D2BedBath.dtype)
# output int64

D2BedBathSlice=  D2BedBath[:1,:5]
print("US Real Estate Price - bed plus bath - Array - Splicing array - D2BedBath[:1,:5] " , D2BedBathSlice)
D2BedBathSlice2=  D2BedBath[:1, 4:15:4]
print("US Real Estate Price - bed plus bath - Array - Splicing array - D2BedBath[:1, 4:15:4] " , D2BedBathSlice2)


# Indexing array
D2BedBathSliceItemOnly=  D2BedBathSlice[0,1]
print("US Real Estate Price - bed plus bath - 2 Dimensional Array - Index array - D2BedBathSlice[1,5] " , D2BedBathSliceItemOnly)
D2BedBathSlice2ItemOnly=  D2BedBathSlice2[0, 2]
print("US Real Estate Price - bed plus bath - 2 Dimensional Array - index array - D2BedBathSlice2[0, 2] " , D2BedBathSlice2ItemOnly)


#You should use the builtin function nditer, if you don't need to have the indexes values.
for elem in np.nditer(D2BedBath):
    print(elem)

#EDIT: If you need indexes (as a tuple for 2D table), then:
for index, elem in np.ndenumerate(D2BedBath):
    print(index, elem)

# 2 x 200 ========>>>>> 1  x 400 - reshape
D2BedBath1TO298 = np.reshape(D2BedBath, (1,400))
print("US Real Estate Price - bed plus bath - 2 Dimensional Array - np.reshape(D2BedBath, (1, 400)) : " , D2BedBath1TO298)
print("US Real Estate Price - bed plus bath - 2 Dimensional Array - np.reshape(D2BedBath, (1, 400)) : Size " , D2BedBath1TO298.size)
print("US Real Estate Price - bed plus bath - 2 Dimensional Array - np.reshape(D2BedBath, (1, 400)) : ndim " , D2BedBath1TO298.ndim)
print("US Real Estate Price - bed plus bath - 2 Dimensional Array - np.reshape(D2BedBath, (1, 400)) : shape " , D2BedBath1TO298.shape)
print("US Real Estate Price - bed plus bath - 2 Dimensional Array - np.reshape(D2BedBath, (1, 400)) : ndim " , D2BedBath1TO298.ndim)




print()