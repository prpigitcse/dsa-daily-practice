"""
Pattern:
Recursion

Problem Statement:
Write a recursive function `is_palindrome(s)` that returns True if the string reads the same forward and backward, and False otherwise. Input: "racecar" → True. Input: "hello" → False. You must use recursion.

Intuition:
Check if $s[\text{left}] = s[\text{right}]$, then recursively check the inner substring $s[\text{left}+1\ldots\text{right}-1]$. The base case is when the pointers cross ($\text{left} \geq \text{right}$) — a single character or empty string is always a palindrome.

Approach:
1. Pass `left` and `right` pointer indices along with the string.
2. Base case: if `left >= right`, return True.
3. If `s[left] != s[right]`, return False immediately.
4. Otherwise, recurse with `left + 1` and `right - 1`.

Time Complexity:
$O(N)$ — at most $\lfloor N/2 \rfloor$ recursive calls, each doing $O(1)$ work

Space Complexity:
$O(N)$ for the recursion call stack ($\lfloor N/2 \rfloor$ frames)

Common Mistakes:
- Not passing the left and right pointers, trying to slice the string instead
- Using `left > right` as the base case instead of `left >= right` (misses the single-character case)
- Forgetting to handle case sensitivity if required
- Creating new string slices at each level, adding $O(N)$ per call

Code Explanation:
- `def check_palindrome(s, left, right)`: Three parameters: the string and two pointer indices. The caller passes `left=0` and `right=len(s)-1`.
- `if left >= right: return True`: **Base case**: pointers have crossed (or met in the middle). The remaining substring is either empty or a single character — both are palindromes.
- `if s[left] != s[right]: return False`: Mismatch found at the outermost unchecked pair; immediately return False without checking inner characters.
- `return check_palindrome(s, left+1, right-1)`: **Recursive case**: outer pair matched; check the next inner pair by moving both pointers inward.
- For `"racecar"` (indices 0–6), it checks `(0,6)='r'/'r'` → `(1,5)='a'/'a'` → `(2,4)='c'/'c'` → `(3,3)` which meets the base case.

Final Thoughts:
This shows how the same algorithm (two-pointer palindrome check) can be expressed iteratively ($O(1)$ space) or recursively ($O(N)$ space). The recursive "check boundaries, recurse inward" pattern also appears in binary search and divide-and-conquer.
"""

# The Problem: Is it a Palindrome? (Recursive)
# Write a function is_palindrome(s) that returns True if the string is a palindrome, and False otherwise.
# Input: "racecar" Output: True
# Input: "hello" Output: False
# Constraint: You must use Recursion. No for/while loops.

def check_palindrome(s, left, right):
    if left >= right:
        return True

    if s[left] != s[right]:
        return False

    return check_palindrome(s, left+1, right-1)

print(check_palindrome("racecar", 0, 6))
print(check_palindrome("hello", 0, 4))