"""
Problem Statement:
Write a recursive function sum_array(arr) that returns the sum of all elements in an array. Input: [1, 2, 3, 4, 5] → Output: 15. Input: [] → Output: 0. No for or while loops allowed — you must use recursion.

Intuition:
The recursive insight is: the sum of an array is the first element plus the sum of the remaining elements. The base case is an empty array, which has a sum of 0. This "peel off the first element" pattern is fundamental to recursive array processing. Each recursive call works on a smaller array until nothing is left.

Approach:
1. Base case: if the array is empty (len(arr) == 0), return 0.
2. Recursive case: return arr[0] + sum_of_array(arr[1:]).
3. arr[1:] creates a new sub-array without the first element, shrinking the problem by one element each time.

Time Complexity:
O(N) where N is the length of the array — one recursive call per element

Space Complexity:
O(N) for the call stack, plus O(N^2) total due to arr[1:] creating a new array copy at each level

Common Mistakes:
- Forgetting the base case for an empty array, leading to infinite recursion
- Using arr[0] without checking if the array is empty first (IndexError)
- Not realizing that arr[1:] creates a new list in Python, adding O(N) work per call — total hidden cost is O(N^2)
- For production code, an iterative sum or Python's built-in sum() is more efficient

Final Thoughts:
This problem teaches you to decompose array operations recursively: process the head, recurse on the tail. While the O(N^2) slicing cost makes this impractical for real use, it builds the recursive thinking pattern needed for more complex problems like merge sort, tree traversals, and divide-and-conquer algorithms.
"""

# The Problem: Sum of Array (Recursive)
# Write a function sum_array(arr) that returns the sum of all elements in an array.
# Input: [1, 2, 3, 4, 5] -> Output: 15
# Input: [] -> Output: 0
# Constraint:You must use Recursion. No for or while loops allowed.

def sum_of_array(arr):
    if len(arr) == 0:
        return 0
    
    return arr[0] + sum_of_array(arr[1:])

print(sum_of_array([1, 2, 3, 4, 5]))
print(sum_of_array([1]))
print(sum_of_array([]))