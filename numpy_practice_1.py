import numpy as np

my_list = [1, 2, 3, 4]
np_my_list = np.array(my_list)
print(np_my_list)

# create zero array
x = np.zeros((4,3))
print(x)

# create ones array
y = np.ones((4, 5))
print(y)

# full array
full = np.full((4, 3), 5)
print(full)
print(full.dtype)

# identity matrix
idm = np.eye(5)
print(idm)

# custom identity matrix
cidm = np.diag([10, 20, 30, 40])
print(cidm)

# print a 1D array with the number of elements
a_range = np.arange(20)
print(a_range)

# convert a_range to 2D array
a_range_2d = np.reshape(a_range, (4, 5))
print("Reshape a_range:")
print(a_range_2d)
print("\n")

# the third parameter - step - determines the number of elements
# if the range is larger than the stop value then only 1 element
a_range = np.arange(2, 10, 30)
print(a_range)

# evenly spaced numbers over an interval
# 0 = starting number, 50 = stop number (inclusive unless endpoint=False)
# 20 = number of items
# dtype = float
lin_space = np.linspace(0, 50, 10)
print("\n")
print(lin_space)

# reshape linspace() array
lin_space_2d = np.linspace(0, 50, 10, endpoint=False, dtype=int).reshape(5, 2)
print("-------")
print(lin_space_2d)
print(lin_space_2d.dtype)

# random number arrays
ran_dom = np.random.random((3, 3))
print("\nRandom array:")
print(ran_dom)

# reshape random array
ran_dom_2d = np.random.random((3, 3)).reshape(1, 9)
print("\n")
print(ran_dom_2d) 
print("ran_dom_2d has shape: ", ran_dom_2d.shape)