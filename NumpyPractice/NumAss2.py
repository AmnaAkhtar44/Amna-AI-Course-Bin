import numpy as np # np is variable name it can be changed , if we used add numpy in file use this code line 

address, latitude , longitude ,price, status, =np.genfromtxt ('Amna-AI-Course-Bin\NumpyPractice\RealEstate-USA (1).csv'  delimiter = ',', usecols=(0,4,5,6), dtype=('U100', 'f8', 'f8', 'f8' ,'U100'),   # force correct types
                                                                encoding='utf-8',unpack=True,skip_header=1 , invalid_raise=False) 
print(address)
print(latitude) # long means longitude north-south position on the earth.
print(longitude) # lat means latitudeid_raise=False)
print(price)
print(status) 

# statistical Operations
print("RealEstate-USA.com price mean:" , np.mean(price))
print("RealEstate-USA.com price median:" , np.median(price))
print("RealEstate-USA.com price  average:" , np.average(price))
print("RealEstate-USA.com price std:" , np.std(price))
print("RealEstate-USA.com price percentile:" , np.percentile(price ,75))
print("RealEstate-USA.com price percentile:" , np.percentile(price, 25))
print("RealEstate-USA.com price percentile:" , np.percentile(price , 3))
print("RealEstate-USA.com price max:" , np.max(latitude))
