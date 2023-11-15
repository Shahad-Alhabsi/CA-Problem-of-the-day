"""
@author: Shahad Al Habsi

problem of the day 15/11/2023:
Given two sorted arrays, metge them in a sorted order without using any extra space.
"""
# read lists from the user
array1 = input("Enter the numbers (separated by a space) for array 1: ").split()
array2 = input("Enter the numbers (separated by a space) for array 2: ").split()
array1 = [int(i) for i in array1]
array2 = [int(i) for i in array2]

# Find intersects in the two lists
array2_copy = array2
intersects = []
for i in range(0,len(array1)):
    if array1[i] in array2 :
        intersect = [array1.index(array1[i]), array2_copy.index(array1[i])]
        if intersect not in intersects:
            intersects.append(intersect)
            array2 = array2[array2_copy.index(array1[i]):]

#print("intersects: " ,intersects)

# find the shortest path    
if len(intersects) == 0:
    path = min(array1, array2_copy)
else:
    path = []
    comulative_sum = 0
    sub_path1 = array1[:intersects[0][0]]
    sub_path2 = array2_copy[:intersects[0][1]]
    shortest_path = sub_path1 if sum(sub_path1)<sum(sub_path2) else sub_path2
    #print(shortest_path, " is the shortest of ", sub_path1 , " and ", sub_path2)
    path += shortest_path
    for j in range(1,len(intersects)):
        sub_path1 = array1[intersects[j-1][0]:intersects[j][0]]
        sub_path2 = array2_copy[intersects[j-1][1]:intersects[j][1]]
        shortest_path = sub_path1 if sum(sub_path1)<sum(sub_path2) else sub_path2
        #print(shortest_path, " is the shortest of ", sub_path1 , " and ", sub_path2)
        path += shortest_path
    sub_path1 = array1[intersects[-1][0]:]
    sub_path2 = array2_copy[intersects[-1][1]:]
    shortest_path = sub_path1 if sum(sub_path1)<sum(sub_path2) else sub_path2
    path += shortest_path
    #print(shortest_path, " is the shortest of ", sub_path1 , " and ", sub_path2)
    
    # print results 
    print("Shortest path is: ", path)
    print("Sum = ", sum(path) )




