"""
@author: Shahad Al Habsi

problem of the day 21/11/2023:


Given an array of size N, find all the elements accuring more than once in the array.
If no such element found return the array [-1]

"""
# validate user input: make sure the input is integers only
while 1:
    try:
        arr = input("Enter the numbers of the list (saparated by a space): ").split()
        arr = [int(i) for i in arr]
        break
    except:
        print("Error! invalid input")

# find repeating elements
res = []
for i in range(len(arr)):
    for j in arr[i+1:]:
        if (arr[i] == j) and (arr[i] not in res):
            res.append(arr[i])
if len(res) == 0:
    print([-1])
else:
    print(res)
            
            
