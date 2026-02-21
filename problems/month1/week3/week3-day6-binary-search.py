"""
Problem Statement:
Given a sorted array arr and a target value, return the index of the target using recursive binary search. If not found, return None. Input: arr = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91], target = 23 → Output: 5. The array MUST be sorted for binary search to work.

Intuition:
Binary search exploits the sorted order to eliminate half the search space with each comparison. Compare the target with the middle element: if equal, we found it; if the target is greater, search the right half; if smaller, search the left half. Recursion naturally expresses this halving — each call works on a shrinking window defined by left and right boundaries.

Approach:
1. Base case: if left > right (or array is empty), return None (target not found).
2. Calculate mid = (left + right) // 2.
3. If arr[mid] == target, return mid.
4. If arr[mid] < target, recurse on the right half: binary_search(arr, target, mid + 1, right).
5. If arr[mid] > target, recurse on the left half: binary_search(arr, target, left, mid - 1).

Time Complexity:
O(log N) — the search space halves with each recursive call

Space Complexity:
O(log N) for the recursion stack (one frame per halving step)

Common Mistakes:
- Using (left + right) / 2 — in some languages this can cause integer overflow; Python handles big integers natively, but it returns a float with /
- Forgetting the base case left > right, causing infinite recursion when the target is not in the array
- Applying binary search to an unsorted array — this produces incorrect results silently
- Using mid - 1 or mid + 1 incorrectly: searching left should use right = mid - 1, right should use left = mid + 1

Final Thoughts:
Binary search is one of the most important algorithms in computer science. It reduces O(N) linear search to O(log N) — for an array of 1 billion elements, that is about 30 comparisons instead of 1 billion. The recursive version makes the halving logic explicit. The iterative version (using a while loop) is often preferred in practice because it avoids the O(log N) stack space.
"""

# The Problem: Search in a Sorted Array
# Given a sorted array arr and a target target, return the index of target. If not found, return None.
# Input: arr = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91], target = 23
# Output: 5 (Index of 23)
# Constraint:
# You must use Recursion.
# If the array is NOT sorted, this algorithm does not work.

def binary_search(arr, target, left, right):
    if not arr or left > right:
        return None
    
    mid = (left + right) // 2

    if arr[mid] == target:
        return mid

    if arr[mid] < target:
        left = mid + 1
    else:
        right = mid - 1

    return binary_search(arr, target, left, right)

print(binary_search([2, 5, 8, 12, 16, 23, 38, 56, 72, 91], 23, 0, 9))
print(binary_search([2, 5, 8, 12, 16, 23, 38, 56, 72, 91], 67, 0, 9))
print(binary_search([2, 5, 8, 12, 16, 23, 38, 56, 72, 91], 2, 0, 9))
print(binary_search([2, 5, 8, 12, 16, 23, 38, 56, 72, 91], 91, 0, 9))
print(binary_search([], 91, 0, 0))
print(binary_search([1, 2, 3], 2, 0, 2))
print(binary_search([1, 2, 3, 4], 3, 0, 3))