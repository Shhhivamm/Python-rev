import numpy as np

# Scalar aritmatics

array = np.array([1,2,3])

# print(array +1)
# print(array +1)
# print(array * 3)
# print(array ** 2)

# Vectorized math function

# print(np.sqrt(array))

num = [4,5,6]

# print(np.round(num))
# print(np.floor(num))
# print(np.ceil(num))


# radius = np.array([2,3,4])

# print( np.pi * radius ** 2)

# print(array + num)
# print(array - num)
# print(array * num)
# print(array / num)
# print(array ** num)


# Comparison operators

scores = np.array([91, 55, 100, 73, 82, 64])

# print(scores >= 60)   

scores[scores < 60] = 0  

print(scores)

