#Write a Python program to repeat a tuple three times using the * operator
my_tuple = (1, 2, 3)
repeated_tuple = my_tuple * 3
print("original tuple:", my_tuple)
print("repeated tuple:", repeated_tuple)

#Write a Python program to join three separate tuples into one new tuple using the + operator.
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
tuple3 = (7, 8, 9)
joined_tuple = tuple1 + tuple2 + tuple3
print("joined tuple:", joined_tuple)

#Write a Python program to check whether a specific element exists inside a tuple using the in keyword.
tuple4 = (1, 2, 3, 4, 5)
element = 3
if element in tuple4:
    print(f"Element {element} exists in the tuple.")
else:
    print(f"Element {element} does not exist in the tuple.")

#Write a Python program to calculate the total, highest value, and lowest value from a tuple of integers without using the built-in sum(), max(), and min() functions
tuple5 = (5, 2, 9, 1, 7)
total = 0
highest = tuple5[0]
lowest = tuple5[0]
for num in tuple5:
    total += num
    if num > highest:
        highest = num
    if num < lowest:
        lowest = num
print("Total:", total)
print("Highest value:", highest)
print("Lowest value:", lowest)

#Write a Python program to filter a tuple . n = (3, 14, 7, 22, 9, 41, 18, 5), keep only values greater than 10
n = (3, 14, 7, 22, 9, 41, 18, 5)
filtered_tuple = tuple(num for num in n if num > 10)
print("Filtered tuple (values greater than 10):", filtered_tuple)

#Write a Python program to determine how many elements are in a set without using the built-in len() function. s = {"cat", "dog", "bird", "fish"}
s = {"cat", "dog", "bird", "fish"}
count = 0
for _ in s:
    count += 1
print("Number of elements in the set:", count)

#Write a Python program to combine two sets into one, containing all unique elements from both sets.
set1 = {"apple", "banana", "cherry"}
set2 = {"banana", "orange", "grape"}
combined_set = set1.union(set2)
print("Combined set:", combined_set)

#Write a Python program to find all elements that are common to both sets. s1 = {1, 2, 3, 4} s2 = {3, 4, 5, 6} 
s1 = {1, 2, 3, 4}
s2 = {3, 4, 5, 6}
common_elements = s1.intersection(s2)
print("Common elements:", common_elements)

#Write a Python program to find all elements that are in either
s1 = {1, 2, 3, 4}
s2 = {3, 4, 5, 6}
either_but_not_both = s1.symmetric_difference(s2)
print("Elements in either set, but not both:", either_but_not_both)
