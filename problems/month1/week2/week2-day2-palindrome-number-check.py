"""
Problem Statement:
Given an integer x, return True if x is a palindrome number, and False otherwise. Do NOT convert the integer to a string. Input: 121 → True. Input: -121 → False (reads as 121- backwards). Input: 10 → False (reads as 01).

Intuition:
Combine the digit extraction technique from Day 1 (Reverse Number) with the palindrome concept from Week 1. Reverse the entire number mathematically, then compare with the original. If they match, it is a palindrome. Negative numbers are never palindromes because the minus sign doesn't mirror.

Approach:
1. If x < 0, return False immediately (negative numbers can't be palindromes).
2. Store the original value of x.
3. Build the reversed number using the digit extraction loop: digit = x % 10, reverse = reverse * 10 + digit, x = x // 10.
4. Compare the reversed number with the original. If equal, return True.

Time Complexity:
O(log N) — proportional to the number of digits

Space Complexity:
O(1) — only integer variables for original, reverse, and digit

Common Mistakes:
- Using str(x) to convert and compare — this violates the constraint
- Forgetting that negative numbers are not palindromes
- Not preserving the original value before modifying x in the loop
- Edge case: 0 is a palindrome (it reads the same both ways)

Final Thoughts:
This problem elegantly combines two concepts: the digit extraction pattern and the palindrome check. It shows how mathematical operations can replace string manipulation, often with better space efficiency. This is a classic LeetCode easy problem (Problem #9).
"""

# The Problem: Palindrome NumberGiven an integer x, return True if x is a palindrome, and False otherwise.
# Input: 121 -> Output: True
# Input: -121 -> Output: False (Reads as 121- from left to right, which is not a valid number).
# Input: 10 -> Output: False (Reads as 01).
# Constraints:Strictly Forbidden: Do not convert the integer to a string. You cannot use str(x).

def is_palindrome(x):
    if x < 0:
        return False
    
    original = x
    reverse = 0
    while x > 0:
        digit = x % 10
        reverse = reverse * 10 + digit
        x = x // 10
    
    return original == reverse

print(is_palindrome(121))
print(is_palindrome(-121))
print(is_palindrome(10))
print(is_palindrome(0))