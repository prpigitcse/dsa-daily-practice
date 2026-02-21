"""
Problem Statement:
Given an array arr, reverse the order of elements in-place. You must modify the original array directly without creating a new array. Input: [10, 20, 30, 40, 50] → Output: [50, 40, 30, 20, 10].

Intuition:
Reversing an array in-place requires the Two-Pointer Technique. Place one pointer at the start and another at the end, then swap and move inward. This avoids allocating a new array, achieving O(1) space. The pattern of "shrinking the window from both ends" is reusable in many problems.

Approach:
1. Initialize two pointers: left = 0, right = len(arr) - 1.
2. While left < right, swap arr[left] and arr[right].
3. Move left one step right and right one step left.
4. Stop when the pointers meet or cross — the array is now reversed.

Time Complexity:
O(N) where N is the length of the array — each element is visited at most once

Space Complexity:
O(1) — the reversal is done in-place using only two pointer variables

Common Mistakes:
- Using left <= right instead of left < right (when pointers meet, swapping the element with itself is harmless but unnecessary)
- Creating a new array (e.g., arr[::-1]) instead of modifying in-place — this uses O(N) extra space
- Forgetting to move both pointers after the swap, causing an infinite loop

Final Thoughts:
The two-pointer technique is one of the most important patterns in DSA. Mastering it here on a simple reversal problem prepares you for harder problems like palindrome checking, container with most water, and two-sum on sorted arrays. Always think "Can I use two pointers?" when dealing with arrays.
"""

# Array Manipulation (In-Place)
# Theme: Modifying memory without using more memory.
# The Problem: Reverse an Array
# Given an array arr, reverse the order of elements in-place.
# Input: [10, 20, 30, 40, 50]
# Output: [50, 40, 30, 20, 10]
# Constraints:You cannot create a new empty array (e.g., new_arr = []) and push items into it. That uses extra memory (O(N) Space).
# You must modify the original array directly (O(1) Space).

# The Logic: The Two-Pointer Technique
# To reverse an array in-place, we use two pointers:
# left: Starts at the beginning of the array (index 0).
# right: Starts at the end of the array (index N-1).
# We swap the elements at the left and right pointers.
# Then, we move the left pointer one step to the right and the right pointer one step to the left.
# We continue this process until the left pointer crosses the right pointer (left >= right).

def reverse_array(arr):
    left = 0
    right = len(arr) - 1
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
    return arr

# Example Usage:
my_array = [10, 20, 30, 40, 50]
print(f"Original array: {my_array}")
reversed_array = reverse_array(my_array)
print(f"Reversed array: {reversed_array}")