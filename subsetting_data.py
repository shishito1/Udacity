import pandas as pd
import numpy as np

data = {
    "name": ["Bella", "Charlie", "Lucy", "Cooper", "Max", "Stella", "Bernie"],
    "breed": ["Labrador", "Poodle", "Chow Chow", "Schnauzer", "Labrador", "Chihuahua", "St. Bernard"],
    "color": ["Brown", "Black", "Brown", "Gray", "Black", "Tan", "White"],
    "height_cm": [56, 43, 46, 49, 59, 18, 77],
    "weight_kg": [25, 23, 22, 17, 29, 2, 74]
}

df = pd.DataFrame(data)

# get rows using loc[] and iloc[]
indexes = [0, 2, 3]
print(df.loc[indexes])

# get rows with a range and default index
# using loc end range is inclusive
print(df.loc[0:3])

# using iloc end range is exclusive
print(df.iloc[0:3, 1:2])

# with a specified index
print("\n--------------")
print("Using set_index() and sort_index() ...")
print("\n--------------")

df_ind = df.set_index("breed").sort_index()
print(df_ind)

# use loc with a defined index (inclusive)
print(df_ind.loc["Chihuahua":"Labrador"])

# use : in column index to get column header
print(df_ind.loc["Chihuahua":"Labrador", "weight_kg":"weight_kg"])

print("\n--------------")

df_ind2 = df.set_index(["breed", "color"]).sort_index()
print(df_ind2)


""" Experimenting with numpy arrays
"""

# create np 2D array
arr = np.array([
    [1, 2, 3, 4, 5], 
    [2, 4, 6, 8, 10],
    [4, 8, 12, 16, 20]])

print("\n--------------")
print("\n--------------")

print(arr)

# create from regular array
arr_normal = [
    [1, 2, 3, 4, 5], 
    [2, 4, 6, 8, 10],
    [4, 8, 12, 16, 20]]

np_arr_normal = np.array(arr_normal)

print("\n")
print(np_arr_normal)

# axis is optional
# requires reshape()
new_row = [1, 1, 0, 1, 1]
np_arr_add = np.append(np_arr_normal, new_row).reshape(4, 5)

print("\n append row")
print(np_arr_add)

# with column axis
np_arr_add_col = np.append(np_arr_normal, [[1], [1], [1]], axis=1)

print("\n append column")
print(np_arr_add_col)

# insert without axis
np_arr_ins = np.insert(np_arr_normal, 5, [1, 1, 1, 1, 1]).reshape(4, 5)
print("\n")
print(np_arr_ins)

# .vstack() : add row
# easier than append
new_row = [8, 16, 24, 32, 40]
np_arr_vstack = np.vstack((np_arr_normal, new_row))
print("\n add row with .vstack()")
print(np_arr_vstack)

# .hstack() : add column
new_col = [[6], [12], [24]]
np_arr_hstack = np.hstack((np_arr_normal, new_col))
print("\n add column with .hstack()")
print(np_arr_hstack)

# diagonal operations
new_row = [16, 32, 48, 64, 80]
np_arr_vstack = np.vstack((np_arr_vstack, new_row))
np_arr_diag = np.diag(np_arr_vstack)
print("\n")
print(np_arr_vstack)
print("\n get diagonals with .diag()")
print(np_arr_diag)

# boolean indexing
# if array contains all numbers
print("\n")
print(np_arr_vstack[np_arr_vstack >= 20])
print(np_arr_vstack[(np_arr_vstack >= 20) & (np_arr_vstack < 50)])

# set operations
# find elements in vstack but not in hstack()
np_arr_diff = np.setdiff1d(np_arr_vstack, np_arr_hstack)
print("\n")
print(np_arr_diff)