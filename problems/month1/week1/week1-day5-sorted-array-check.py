"""
Pattern:
Array

Problem Statement:
Write a function that returns True if an array is sorted in ascending order, and False otherwise. For example, [1, 2, 3, 4, 5] returns True, while [1, 2, 3, 5, 4] returns False.

Intuition:
A sorted array has the property that every element is less than or equal to the next one: $a_i \leq a_{i+1}$ for all $i$. We only need to find a **single violation** to prove the array is unsorted. This is the "early exit" pattern — return False immediately upon finding the first violation.

Approach:
1. Iterate through indices $0$ to $N-2$ (using `range(len(arr) - 1)`).
2. At each position, compare `arr[i]` with `arr[i+1]`.
3. If `arr[i] > arr[i+1]`, the array is not sorted — return False immediately.
4. If the loop completes without finding any violations, return True.

Time Complexity:
$O(N)$ in the worst case (fully sorted array), but can exit early in practice

Space Complexity:
$O(1)$ — only loop variables are used

Common Mistakes:
- Using `range(len(arr))` instead of `range(len(arr) - 1)`, causing an index-out-of-bounds error when accessing `arr[i+1]`
- Not handling edge cases: an empty array `[]` or single-element array `[5]` should both return True
- Checking strict less-than (`<`) instead of less-than-or-equal (`<=`), incorrectly marking `[1, 1, 2]` as unsorted

Code Explanation:
- `def sorted_array_check(arr)`: Takes the array to check.
- `for i in range(len(arr) - 1)`: Iterates from index 0 to the second-to-last element; stops one short so `arr[i+1]` is always valid.
- `if arr[i] > arr[i + 1]`: Compares adjacent elements; `>` (not `>=`) allows equal consecutive values.
- `return False`: Returns immediately on the first violation (early exit).
- `return True`: Only reached if no violations were found; the array is sorted.

Final Thoughts:
The early exit pattern is a powerful optimization. In the best case, you find a violation at the very first pair and return in $O(1)$ time. This "fail fast" approach appears frequently in validation problems.
"""

# Question: Write a function that returns True if an array is sorted in ascending order, and False otherwise.

def sorted_array_check(arr):
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return False
    return True

my_array = [1, 2, 3, 5, 4]
print(f"Is the array sorted? {sorted_array_check(my_array)}")
