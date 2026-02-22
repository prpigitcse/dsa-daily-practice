"""
Problem Statement:
Given an array `arr`, reverse the order of elements in-place. You must modify the original array directly without creating a new array. Input: [10, 20, 30, 40, 50] → Output: [50, 40, 30, 20, 10].

Intuition:
Reversing an array in-place uses the **Two-Pointer Technique**. Place one pointer at the start (`left = 0`) and another at the end (`right = N-1`), then swap and move inward. This avoids allocating a new array, achieving $O(1)$ space.

Approach:
1. Initialize two pointers: `left = 0`, `right = len(arr) - 1`.
2. While `left < right`, swap `arr[left]` and `arr[right]`.
3. Move `left` one step right and `right` one step left.
4. Stop when the pointers meet or cross — the array is now reversed.

Time Complexity:
$O(N)$ where $N$ is the length of the array — each element is visited at most once

Space Complexity:
$O(1)$ — the reversal is done in-place using only two pointer variables

Common Mistakes:
- Using `left <= right` instead of `left < right` (when pointers meet, swapping an element with itself is harmless but unnecessary)
- Creating a new array (e.g., `arr[::-1]`) instead of modifying in-place — this uses $O(N)$ extra space
- Forgetting to move both pointers after the swap, causing an infinite loop

Code Explanation:
- `def reverse_array(arr)`: Takes the array to reverse; modifies it in-place.
- `left = 0`: Starts the left pointer at the first element.
- `right = len(arr) - 1`: Starts the right pointer at the last element (index is length minus 1).
- `while left < right`: Continues until the two pointers meet in the middle.
- `arr[left], arr[right] = arr[right], arr[left]`: Python's simultaneous assignment swaps both elements without a temporary variable.
- `left += 1` and `right -= 1`: Advance both pointers inward for the next iteration.
- `return arr`: Returns the same array object (modified in-place).

Final Thoughts:
The two-pointer technique is one of the most important patterns in DSA. Mastering it here on a simple reversal problem prepares you for harder problems like palindrome checking, container with most water, and two-sum on sorted arrays.
"""

# Array Manipulation (In-Place)
# Given an array arr, reverse the order of elements in-place.

def reverse_array(arr):
    left = 0
    right = len(arr) - 1
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
    return arr

my_array = [10, 20, 30, 40, 50]
print(f"Original array: {my_array}")
reversed_array = reverse_array(my_array)
print(f"Reversed array: {reversed_array}")