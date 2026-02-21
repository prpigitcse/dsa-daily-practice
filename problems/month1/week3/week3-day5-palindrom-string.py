"""
Problem Statement:
Write a recursive function is_palindrome(s) that returns True if the string reads the same forward and backward, and False otherwise. Input: "racecar" → True. Input: "hello" → False. You must use recursion — no for/while loops allowed.

Intuition:
This combines the recursive thinking from this week with the two-pointer palindrome logic from Week 1. Instead of using a while loop with left/right pointers, we recurse: check if the outermost characters match, then recursively check the substring between them. The base case is when the pointers cross (a single character or empty string is always a palindrome).

Approach:
1. Pass left and right pointer indices along with the string.
2. Base case: if left >= right, return True (we have checked all pairs).
3. If s[left] != s[right], return False immediately.
4. Otherwise, recurse with left + 1 and right - 1.

Time Complexity:
O(N) — at most N/2 recursive calls, each doing O(1) work

Space Complexity:
O(N) for the recursion call stack (N/2 frames)

Common Mistakes:
- Not passing the left and right pointers, trying to slice the string instead (creates unnecessary copies)
- Using left > right as the base case instead of left >= right (misses the single-character case)
- Forgetting to handle case sensitivity (if required by the problem)
- Creating new string slices at each level, which adds O(N) per call

Final Thoughts:
This problem beautifully demonstrates how the same algorithm (two-pointer palindrome check) can be expressed both iteratively and recursively. The iterative version is more space-efficient (O(1) vs O(N)), but the recursive version reinforces the pattern of "check the boundaries, then recurse inward." This same recursive shrinking appears in binary search and divide-and-conquer.
"""

# The Problem: Is it a Palindrome? (Recursive)
# Write a function is_palindrome(s) that returns True if the string is a palindrome, and False otherwise.
# Input: "racecar" Output: True
# Input: "hello" Output: False
# Constraint:You must use Recursion. No for/while loops.

def check_palindrome(s, left, right):
    if left >= right:
        return True

    if s[left] != s[right]:
        return False

    return check_palindrome(s, left+1, right-1)

print(check_palindrome("racecar", 0, 6))
print(check_palindrome("hello", 0, 4))