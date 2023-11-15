"""
@author: Shahad AlHabsi

Problem of the day 14/11/2023
"""


# read the grid from the user
rows= input("Constructing the grid: \nHow namy rows does your grid have? ")
grid = []
for r in range(int(rows)):
    new_row = input("Enter the numbers in row "+str(r)+ "(separated by a space): ").split()
    integer_row= [int(i) for i in new_row]
    grid.append(integer_row)
print("\nyour grid:")
for g in grid:
    print(g)
    
# the biggest number is the value we are looking for
biggest_value = max(grid[0])
for i in range(1,int(rows)):
    if max(grid[i]) > biggest_value:
        biggest_value = max(grid[i])
    

#Look for the number befor the biggest value 
before_value = biggest_value - 1

#Find the indices for both values to find the direction
biggest_value_index = [[i, e.index(biggest_value)] for i, e in enumerate(grid) if biggest_value in e][0]
before_value_index = [[i, e.index(before_value)] for i, e in enumerate(grid) if before_value in e][0]

# if the values are in the same row, the direction is either left or right
if biggest_value_index[0] == before_value_index[0]:
    if biggest_value_index[1] > before_value_index[1]:
        direction = "right"
    else:
       direction = "left" 
else:   
    if biggest_value_index[1] == before_value_index[1]:
        if biggest_value_index[0] > before_value_index[0]:
            direction = "down"
        else:
           direction = "up" 

#print result
print(biggest_value, direction)













