"""
Pattern:
Basic Search

Problem Statement:
Given an array `arr[]` and an integer `target`, return the index of the target element. If the target is not found, return -1. The array is not necessarily sorted.

Intuition:
Linear search is the most fundamental searching algorithm. Since we have no information about the ordering of elements, we must check every element one by one. The key insight is that this is the best we can do for an unsorted array — there is no shortcut below $O(N)$ without additional structure.

Approach:
1. Iterate through the array using `enumerate` to get both the index and value.
2. At each position, compare the current element with the target.
3. If they match, immediately return the current index.
4. If the loop completes without finding the target, return -1.

Time Complexity:
$O(N)$ where $N$ is the length of the array — in the worst case, we check every element

Space Complexity:
$O(1)$ — no extra space is used beyond loop variables

Common Mistakes:
- Returning 0 instead of -1 when the element is not found (0 is a valid index)
- Not handling empty arrays (the loop simply doesn't execute and returns -1 correctly)
- Forgetting to return immediately when the element is found, causing unnecessary iterations

Code Explanation:
- `def linear_search(arr, target)`: Takes the array and the value to search for.
- `for i, j in enumerate(arr)`: `enumerate` yields `(index, value)` pairs; `i` is the position, `j` is the element.
- `if j == target`: Compares the current element to the target value.
- `return i`: Immediately returns the index as soon as the target is found (early exit).
- `return -1`: Reached only if the loop finishes without a match; -1 signals "not found".

Final Thoughts:
Linear search is simple but important. It establishes the baseline: $O(N)$ for searching an unsorted array. Later, Binary Search achieves $O(\log N)$ — but only on sorted arrays. Understanding this trade-off is fundamental to choosing the right algorithm.
"""

# Linear Search (Traversal)
# Question: Given an array arr[] and an integer target, return the index of the target. If the target is not found, return -1.

def linear_search(arr, target):
    for i, j in enumerate(arr):
        if j == target:
            return i
    return -1

print(linear_search([1, 2, 3, 4, 5], 3))
print(linear_search([1, 2, 3, 4, 5], 6))
