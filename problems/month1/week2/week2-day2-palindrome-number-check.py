"""
Problem Statement:
Given an integer, determine if it is a palindrome. An integer is a palindrome if it reads the same forward and backward. For example, 121 is a palindrome; -121 and 10 are not. Return True or False.

Intuition:
Just like reversing a number, we extract digits one by one using modulo. We don't need to fully reverse the number — we can compare the reversed number to the original. Negative numbers are never palindromes (due to the plus sign), and numbers ending in 0 (except 0 itself) are never palindromes.

Approach:
1. Return False immediately for negative numbers.
2. Return False for numbers that end in 0 but aren't 0 themselves.
3. Extract digits one at a time to build `reversed_num`.
4. Compare `reversed_num` with the original `n` — if equal, it's a palindrome.

Time Complexity:
$O(\log_{10} N)$ — number of digits in $N$

Space Complexity:
$O(1)$ — only integer variables

Common Mistakes:
- Converting to a string (`str(n) == str(n)[::-1]`) — valid but not a true mathematical solution
- Not handling negative numbers: they have a `-` prefix so can never be palindromes
- Not handling numbers ending in 0: `10` reversed is `01 = 1`, not `10`, so it's not a palindrome

Code Explanation:
- `if n < 0: return False`: Negative numbers always fail due to the `-` sign.
- `if n != 0 and n % 10 == 0: return False`: A trailing zero can't be mirrored at the start of a positive integer.
- `original = n`: Save the original value for comparison at the end.
- `reversed_num = 0`: Accumulator for the reversed number.
- `while n > 0`: Loop while digits remain.
- `reversed_num = reversed_num * 10 + n % 10`: Extract the last digit and append it to `reversed_num`.
- `n = n // 10`: Chop off the last digit.
- `return reversed_num == original`: True if the reversed number equals the original.

Final Thoughts:
This builds directly on Day 1 (Reverse Number). A palindrome check is a reversal check — the reversed number equals the original. The early exits for negatives and trailing zeros make the solution more robust.
"""

# Week 2 Day 2: Palindrome Number Check
# Given an integer, determine if it is a palindrome.

def palindrome_number_check(n):
    if n < 0:
        return False
    if n != 0 and n % 10 == 0:
        return False
    original = n
    reversed_num = 0
    while n > 0:
        reversed_num = reversed_num * 10 + n % 10
        n = n // 10
    return reversed_num == original

print(palindrome_number_check(121))   # True
print(palindrome_number_check(-121))  # False
print(palindrome_number_check(10))    # False