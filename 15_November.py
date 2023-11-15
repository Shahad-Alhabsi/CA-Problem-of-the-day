"""
@author: Shahad Al Habsi

problem of the day 15/11/23:
Given two sorted arrays, metge them in a sorted order without using any extra space.
"""

#read the two arrays from the user
array1 = input("Enter the numbers (separated by a space) for array 1: ").split()
array2 = input("Enter the numbers (separated by a space) for array 2: ").split()
array1 = [int(i) for i in array1]
array2 = [int(i) for i in array2]

#insert the values of the first array in the second array while keeping it sorted
for i in array1:
    for j in array2:
        if i >= array2[-1]:
            array2.append(i)
        else:
            if i < j:
                array2.insert(array2.index(j),i)
                break

# print the second array after inserting
for i in range(len(array2)-1):
    print(array2[i]," , ",end="")
print(array2[-1])
