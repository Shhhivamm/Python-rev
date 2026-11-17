import numpy as np


ages = np.array([[21,17,19,20,16,30,18,65],
                 [39,22,15,99,78,19,20,21]])

teenagers = ages[ages < 18]
# adult = ages[(ages >= 18) & (ages <= 60)]
adult = np.where(ages >= 18, ages, 0)
seniors = ages[ages >= 60]
# print(teenagers)
print(adult)
# print(seniors)