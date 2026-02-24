"""
Pattern:
Two Pointers

Problem Statement:
Given a string, return True if it reads the same forward and backward, and False otherwise. For example, "racecar" is a palindrome, "hello" is not. A single character like "a" is always a palindrome.

Intuition:
A palindrome is symmetric: $s[i] = s[N-1-i]$ for all $i$. This is the same two-pointer technique used for array reversal — compare from both ends and move inward. Finding any mismatch lets us immediately return False (early exit).

Approach:
1. Initialize two pointers: `left = 0`, `right = len(s) - 1`.
2. While `left < right`, compare `s[left]` with `s[right]`.
3. If they differ, return False immediately.
4. If they match, move `left` forward and `right` backward.
5. If the loop completes without mismatches, return True.

Time Complexity:
$O(N)$ where $N$ is the length of the string — at most $\lfloor N/2 \rfloor$ comparisons

Space Complexity:
$O(1)$ — only two pointer variables, no extra data structures

Common Mistakes:
- Comparing with `s == s[::-1]` — correct but uses $O(N)$ extra space
- Not handling case sensitivity: "Racecar" returns False unless normalized to lowercase first
- Forgetting edge cases: empty string `""` and single character `"a"` are both palindromes

Code Explanation:
- `def palindrom_check(s)`: Takes the string to check. (Note: the function name has a deliberate typo — `palindrom` instead of `palindrome`.)
- `left = 0` and `right = len(s) - 1`: Initialize both pointers at opposite ends of the string.
- `while left < right`: Stops when pointers would overlap; the middle character (for odd-length strings) doesn't need checking.
- `if s[left] != s[right]: return False`: Mismatch found; immediately signals not a palindrome.
- `left += 1` and `right -= 1`: Move both pointers inward for the next comparison.
- `return True`: All pairs matched; the string is a palindrome.

Final Thoughts:
This problem reinforces the two-pointer pattern from Day 4 (Array Reversal). Strings in Python are essentially character arrays, so the same pointer logic applies.
"""

# Question: Given a string (e.g., "racecar" or "hello"), return True if it reads the same forward and backward.

def palindrom_check(s):
    left = 0
    right = len(s) - 1

    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True

print(palindrom_check("racecar"))  # True
print(palindrom_check("hello"))    # False
print(palindrom_check("a"))        # True