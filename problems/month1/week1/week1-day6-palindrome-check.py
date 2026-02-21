"""
Problem Statement:
Given a string, return True if it reads the same forward and backward, and False otherwise. For example, "racecar" is a palindrome, "hello" is not. A single character like "a" is always a palindrome.

Intuition:
A palindrome is symmetric: the first character must equal the last, the second must equal the second-to-last, and so on. This is the exact same two-pointer technique used for array reversal — compare from both ends and move inward. If any pair mismatches, we can immediately return False.

Approach:
1. Initialize two pointers: left = 0, right = len(s) - 1.
2. While left < right, compare s[left] with s[right].
3. If they differ, return False immediately (not a palindrome).
4. If they match, move left forward and right backward.
5. If the loop completes without mismatches, return True.

Time Complexity:
O(N) where N is the length of the string — at most N/2 comparisons

Space Complexity:
O(1) — only two pointer variables, no extra data structures

Common Mistakes:
- Comparing with s == s[::-1] — while correct, it uses O(N) extra space and doesn't demonstrate the two-pointer technique
- Not handling case sensitivity: "Racecar" would return False unless you normalize to lowercase first
- Forgetting edge cases: empty string "" and single character "a" are both palindromes

Final Thoughts:
This problem reinforces the two-pointer pattern from Day 4 (Array Reversal). Strings in Python are essentially character arrays, so the same pointer logic applies. The early-exit optimization means we stop as soon as we find the first mismatch, making this efficient in practice.
"""

# Question: Given a string (e.g., "racecar" or "hello"), return True if it reads the same forward and backward.

# Explanation & Logic:

# Strings are essentially character arrays. This is the same logic as Day 4 (Reverse Array).

# The Logic: Compare the first char with the last char. If they match, move inward. If they don't match, stop immediately and return False.

# Edge Case: A single character ("a") is always a palindrome.

def palindrom_check(s):
    left = 0
    right = len(s) - 1

    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True

# Test Cases
print(palindrom_check("racecar"))  # True
print(palindrom_check("hello"))    # False
print(palindrom_check("a"))        # True