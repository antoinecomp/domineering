import numpy as np
x = np.ones((3,3)) # what does that stands for ?
print("Checkerboard pattern:")
x = np.zeros((8,8),dtype=int)
# warning, [ordinates in reverse,abscisses]
x [1,1] = 1
x [0,1] = 1
x[6,7] = 2
x[6,6] = 2
print(x)
