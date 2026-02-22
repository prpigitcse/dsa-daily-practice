"""
Problem Statement:
Write a recursive function `sum_array(arr)` that returns the sum of all elements in an array. Input: [1, 2, 3, 4, 5] → Output: 15. Input: [] → Output: 0. No for or while loops allowed.

Intuition:
The recursive insight: $\text{sum}([a_0, a_1, \ldots, a_{N-1}]) = a_0 + \text{sum}([a_1, \ldots, a_{N-1}])$. The base case is an empty array with sum 0. This "peel off the first element" pattern is fundamental to recursive array processing.

Approach:
1. Base case: if `len(arr) == 0`, return 0.
2. Recursive case: return `arr[0] + sum_of_array(arr[1:])`.
3. `arr[1:]` creates a new sub-array, shrinking the problem by one element each call.

Time Complexity:
$O(N)$ — one recursive call per element

Space Complexity:
$O(N)$ for the call stack, plus a hidden $O(N^2)$ total cost due to `arr[1:]` creating a new array copy at each level

Common Mistakes:
- Forgetting the base case for an empty array, leading to infinite recursion
- Using `arr[0]` without checking if the array is empty first (IndexError)
- Not realizing `arr[1:]` costs $O(N)$ per call — hidden total cost is $O(N^2)$
- For production code, Python's built-in `sum()` is more efficient

Code Explanation:
- `def sum_of_array(arr)`: Recursive function that accepts the current sub-array to sum.
- `if len(arr) == 0: return 0`: **Base case**: empty array has a sum of 0. This stops the recursion.
- `return arr[0] + sum_of_array(arr[1:])`: **Recursive case**: take the first element `arr[0]`, then recursively sum the rest of the array `arr[1:]` (a new list from index 1 onward).
- For `sum_of_array([1, 2, 3])`: `1 + sum_of_array([2, 3])` → `1 + 2 + sum_of_array([3])` → `1 + 2 + 3 + sum_of_array([])` → `1 + 2 + 3 + 0 = 6`.
- `arr[1:]`: Python slice notation creates a new list excluding the first element; it's evaluated fresh on each call.

Final Thoughts:
This problem teaches recursive decomposition: process the head, recurse on the tail. While $O(N^2)$ slicing makes it impractical for real use, it builds the recursive thinking needed for merge sort, tree traversals, and divide-and-conquer.
"""

# The Problem: Sum of Array (Recursive)
# Write a function sum_array(arr) that returns the sum of all elements in an array.
# Input: [1, 2, 3, 4, 5] -> Output: 15
# Input: [] -> Output: 0
# Constraint: You must use Recursion. No for or while loops allowed.

def sum_of_array(arr):
    if len(arr) == 0:
        return 0
    
    return arr[0] + sum_of_array(arr[1:])

print(sum_of_array([1, 2, 3, 4, 5]))
print(sum_of_array([1]))
print(sum_of_array([]))