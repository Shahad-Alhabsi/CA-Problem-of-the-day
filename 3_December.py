"""
Proplem of the day:  Dec 3 2023

@author: Shahad Mansoor AlHabsi
"""

def sumUpToZero(list_in):
    for i in range(0, len(list_in)-2):
        for j in range(i+1 ,len(list_in)-1):
            for k in range(j+1, len(list_in)):
                if list_in[i] + list_in[j] + list_in[k] == 0:
                    return "1"
    return "0"
                
                
                
