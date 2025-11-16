import numpy as np # np is variable name it can be changed , if we used add numpy in file use this code line 

address, latitude , longitude , name, =np.genfromtxt('Amna-AI-Course-Bin/NumpyPractice/FastFoodRestaurants (1).csv', delimiter = ',', usecols=(0,4,5,6), dtype=('U100', 'f8', 'f8', 'U100'),   # force correct types
                                                                encoding='utf-8',unpack=True,skip_header=1 , invalid_raise=False)
print(address)
print(latitude) # long means longitude north-south position on the earth.
print(longitude) # lat means latitude
print(name) 

# statistical Operations
print("FastFoodRestaurants.com price mean:" , np.mean(latitude))
print("FastFoodRestaurants.com price median:" , np.median(latitude))
print("FastFoodRestaurants.com price average:" , np.average(latitude))
print("FastFoodRestaurants.com price std:" , np.std(latitude))
print("FastFoodRestaurants.com price percentile:" , np.percentile(latitude ,75))
print("FastFoodRestaurants.com price percentile:" , np.percentile(latitude, 25))
print("FastFoodRestaurants.com price percentile:" , np.percentile(latitude , 3))
print("FastFoodRestaurants.com price max:" , np.max(latitude))
