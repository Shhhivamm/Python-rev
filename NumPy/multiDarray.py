import numpy as np

array = np.array(['a', 'b','c'])
array2 = np.array([['a', 'b','c'],
                   ['d','e','f']])

array3= np.array([
    [
        [1, 2, 3],
        [4, 5, 6]
    ],
    [
        [7, 8, 9],
        [10, 11, 12]
    ]
])

print(array.ndim)
print(array2.ndim)
print(array3.ndim)
print(array3.shape)

print(array3[0][0][0])  #Chain Indexing
print(array3[0,0,1]) #Multidimensional indexing