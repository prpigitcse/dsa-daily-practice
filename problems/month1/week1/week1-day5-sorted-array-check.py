"""
Problem Statement:
Write a function that returns True if an array is sorted in ascending order, and False otherwise. For example, [1, 2, 3, 4, 5] returns True, while [1, 2, 3, 5, 4] returns False.

Intuition:
A sorted array has the property that every element is less than or equal to the next one. We only need to find a SINGLE violation to prove the array is unsorted. This is the "Early Exit" pattern — we return False immediately upon finding the first violation, without needing to check the rest of the array.

Approach:
1. Iterate through the array from index 0 to len(arr) - 2.
2. At each position, compare arr[i] with arr[i+1].
3. If arr[i] > arr[i+1], the array is not sorted — return False immediately.
4. If the loop completes without finding any violations, return True.

Time Complexity:
O(N) in the worst case (fully sorted array), but can be faster in practice due to early exit

Space Complexity:
O(1) — only loop variables are used

Common Mistakes:
- Using range(len(arr)) instead of range(len(arr) - 1), causing an index-out-of-bounds error when accessing arr[i+1]
- Not handling edge cases: an empty array [] or single-element array [5] should both return True
- Checking for strict less-than (<) instead of less-than-or-equal (<=), incorrectly marking [1, 1, 2] as unsorted

Final Thoughts:
The early exit pattern is a powerful optimization strategy. In the best case, you find the violation at the very first pair and return in O(1) time. This "fail fast" approach appears frequently in validation problems and is worth internalizing.
"""

# Question: Write a function that returns True if an array is sorted in ascending order, and False otherwise.

# Explanation & Logic:

# This tests "Early Exit" logic.

# The Logic: Iterate through the array comparing the current element arr[i] with the next element arr[i+1].

# The Key: As soon as you find a SINGLE pair where arr[i] > arr[i+1], you know the array is broken. You should return False immediately. If you finish the loop without issues, return True.

def sorted_array_check(arr):
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return False
    return True

# Example Usage:
my_array = [1, 2, 3, 5, 4]
print(f"Is the array sorted? {sorted_array_check(my_array)}")
