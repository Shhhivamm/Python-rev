import numpy as np

array = np.array([[1,2,3,4,5],
                  [6,7,8,9,10]])

print("Sum of array: ",np.sum(array))
print("mean of array: ",np.mean(array))
print("standard deviation: ",np.std(array))
print("variance: ",np.var(array))
print("minimum: ",np.min(array))
print("maximum: ",np.max(array))
print("position of min value: ",np.argmin(array))

print(np.sum(array, axis=1))