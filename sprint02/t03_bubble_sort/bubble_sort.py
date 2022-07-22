# Sorting is a basic building block for building algorithms

## Importance of Sorting Algorithms 
# By sorting a list of items you will be able to perform the folowing operations:
# searching - search for an item in a list
# selection - selecting items from a list based on their relationship to the rest of the items
# duplicates - finding duplicate values on a list 
# distribution - snalyzing the frequency distribution of items on a list

# Built-In Sorting in Python use the sorted() function
# example:
# list = [8, 2, 6, 4, 5]
# sorted(list) # asending is default (for desending: sorted(list, reverse=true))
# output
# [2, 4, 5, 6, 8]


# Most popular Sorting algorithms
# bubble sort
# selection sort
# insertion sort

# Bubble sort
# https://www.geeksforgeeks.org/sorting-algorithms-in-python/
# Bubble Sort is a simple sorting algorithm.
# This sorting algorithm repeatedly compares two adjacent elements and 
# ... swaps them if they are in the wrong order.
# It is also known as the sinking sort.

# Bubble sort can be visualized as a queue 
# ... where people arrange themselves by swapping with each other 
# ... so that they all can stand in ascending order of their heights.

# This means, we compare two adjacent elements and see if their order is wrong, 
# ... if the order is wrong we swap them.
# arr[i] > arr[j] for 1 <= i < j <= s; 
# where s is the size of the array, if array is to be in ascending order, and vice-versa).

# Example: sort the following sequence using bubble sort
# Sequence: 2, 23, 10, 1

# First Iteration: (first cycle/loop)
# (2, 23, 10, 1) –> (2, 23, 10, 1) 
# the first 2 elements are compared and remain the same 
# ... because they are already in ascending order
# (2, 23, 10, 1) –> (2, 10, 23, 1)
# 2nd and 3rd elements are compared and swapped
# ... (10 is less than 23) according to ascending order
# (2, 10, 23, 1) –> (2, 10, 1, 23)
# 3rd and 4th elements are compared and swapped
# ... (1 is less than 23) according to ascending order
#
# Second Iteration: (second cycle/loop)
# (2, 10, 1, 23) –> (2, 10, 1, 23)
# the first 2 elements are compared and remain the same 
# ... because they are already in ascending order
# (2, 10, 1, 23) –> (2, 1, 10, 23)
# 2nd and 3rd elements are compared and swapped
# ... (1 is less than 10) in ascending order
# 
# Third Iteration (third cycle/loop)
# (2, 1, 10, 23) –> (1, 2, 10, 23)
# the first 2 elements are compared and swap according to ascending order.
# 
# Final result is 1, 2, 10, 23.

# Implementation of Bubble Sort:
# def bubbleSort(arr):
#     n = len(arr)
#     # Use a 'For' loop to go through all elements in the array
#     for i in range(n):
#         for j in range(0, n - i - 1):
#             # Range of the array is from 0 to n-i-1
#             # Swap the elements if the element found is greater than the adjacent element
#             if arr[j] > arr[j + 1]:
#                 arr[j], arr[j + 1] = arr[j + 1], arr[j]
#                  
# Example to test the above code
# arr = [ 2, 1, 10, 23 ]
# bubbleSort(arr)
# print(f"Sorted array is: {arr}")  

# pros and cons of using bubble sort:
# pro: it is simple to understand
# cons: the runtime (time-complexity) is very slow when using large data set

# selection sort
# https://www.geeksforgeeks.org/sorting-algorithms-in-python/
# Repeatedly finds the minimum element in list and sort it in ascending order

# insertion sort
# https://www.geeksforgeeks.org/sorting-algorithms-in-python/
# Maintains a sub-array that always sort elements in a list and place them in the correct order



def bubble_sort(arr):
    n = len(arr)
    # Use a 'For' loop to go through all elements in the array
    for i in range(n):
        for j in range(0, n - i - 1):  # Range of the array is from 0 to n-i-1
            # Swap the elements if the element found is greater than the adjacent element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                 












