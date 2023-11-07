"""  -> The deepcopy function is used to create a deep copy of an object.
    ->  A deep copy of an object creates a new object with new references
        for all objects contained within the original object.
    -> This means that changes made to objects within the deep copy do
        not affect the original object or any other copies.
    -> Deep copies are useful when you want to completely duplicate an object.
"""
import  copy
print("\n--- Using (deepcopy) ---")
j = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
k = copy.deepcopy(j)
k[1][2] = 100
print(f"Original = {j}")  # [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(f"Deep Copy = {k}")  # [[1, 2, 3], [4, 5, 100], [7, 8, 9]]