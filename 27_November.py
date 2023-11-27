"""
@author: Shahad Al Habsi

problem of the day 27/11/2023:


Given an array of integers representing the histograms heights when the width of each is 1.
return the area of the largest rectangle in the histogram.

"""

def largestRectangle(histogram):
    rectangles = []
    for i in range(len(histogram)-1):
        rectangles.append(min(histogram[i], histogram[i+1])*2)
    print(rectangles)
    return max(rectangles)
        

test_case = [2,1,5,6,2,3]
print(largestRectangle(test_case))        
        
        