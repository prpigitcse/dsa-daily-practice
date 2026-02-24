"""
Pattern:
Binary Search

Problem Statement:
Given a sorted array `arr` and a target value, return the index of the target using recursive binary search. If not found, return None. Input: arr = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91], target = 23 → Output: 5.

Intuition:
Binary search exploits sorted order to eliminate half the search space with each comparison. Compare target to the middle element $\text{arr}[\text{mid}]$: if equal, found; if $\text{target} > \text{arr}[\text{mid}]$, search right half; otherwise left half. Each recursive call works on a shrinking window of size $\lfloor N/2 \rfloor$.

Approach:
1. Base case: if `left > right`, return None (target not found).
2. Calculate $\text{mid} = \lfloor (\text{left} + \text{right}) / 2 \rfloor$.
3. If `arr[mid] == target`, return `mid`.
4. If `arr[mid] < target`, recurse on right: `binary_search(arr, target, mid + 1, right)`.
5. If `arr[mid] > target`, recurse on left: `binary_search(arr, target, left, mid - 1)`.

Time Complexity:
$O(\log N)$ — the search space halves with each recursive call

Space Complexity:
$O(\log N)$ for the recursion stack (one frame per halving step)

Common Mistakes:
- Using `(left + right) / 2` instead of `//` (returns a float in Python)
- Forgetting the base case `left > right`, causing infinite recursion
- Applying binary search to an unsorted array — produces incorrect results silently
- Off-by-one: searching left uses `right = mid - 1`, right uses `left = mid + 1`

Code Explanation:
- `def binary_search(arr, target, left, right)`: Takes the array, target value, and the current search window `[left, right]`.
- `if not arr or left > right: return None`: **Base case 1**: empty array guard; **base case 2**: window collapsed (target not in array).
- `mid = (left + right) // 2`: Integer floor division finds the middle index. `//` prevents float results.
- `if arr[mid] == target: return mid`: **Found**: return the index directly.
- `if arr[mid] < target: left = mid + 1`: Target is in the right half; narrow the window by moving `left` past `mid`.
- `else: right = mid - 1`: Target is in the left half; narrow by moving `right` before `mid`.
- `return binary_search(arr, target, left, right)`: Recurse with the updated (halved) window.

Final Thoughts:
Binary search reduces $O(N)$ linear search to $O(\log N)$. For 1 billion elements, that is ~30 comparisons instead of 1 billion. The iterative version (using `while`) is preferred in practice to avoid the $O(\log N)$ stack overhead.
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