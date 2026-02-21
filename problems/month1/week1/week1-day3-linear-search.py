"""
Problem Statement:
Given an array arr[] and an integer target, return the index of the target element. If the target is not found in the array, return -1. The array is not necessarily sorted.

Intuition:
Linear search is the most fundamental searching algorithm. Since we have no information about the ordering of elements, we must check every element one by one. The key insight is that this is the best we can do for an unsorted array — there is no shortcut.

Approach:
1. Iterate through the array using enumerate to get both the index and value.
2. At each position, compare the current element with the target.
3. If they match, immediately return the current index.
4. If the loop completes without finding the target, return -1.

Time Complexity:
O(N) where N is the length of the array — in the worst case, we check every element

Space Complexity:
O(1) — no extra space is used beyond loop variables

Common Mistakes:
- Returning 0 instead of -1 when the element is not found (0 is a valid index)
- Not handling empty arrays (the loop simply doesn't execute and returns -1 correctly)
- Forgetting to return immediately when the element is found, causing unnecessary iterations

Final Thoughts:
Linear search is simple but important to understand. It establishes the baseline complexity for searching: O(N). Later, you will learn Binary Search which achieves O(log N) — but only works on sorted arrays. Understanding this trade-off is fundamental to choosing the right algorithm.
"""

# Linear Search (Traversal)
# Question: Given an array arr[] and an integer target, return the index of the target. If the target is not found, return -1.
# Explanation & Logic:This is the most fundamental searching algorithm.The Logic: You must visit every element one by one (iteration).Constraint: You cannot assume the array is sorted. Therefore, in the worst case (the item is at the end or missing), you must look at N items. This is O(N) complexity.

def linear_search(arr, target):
    for i, j in enumerate(arr):
        if j == target:
            return i
    return -1

print(linear_search([1, 2, 3, 4, 5], 3))
print(linear_search([1, 2, 3, 4, 5], 6))
