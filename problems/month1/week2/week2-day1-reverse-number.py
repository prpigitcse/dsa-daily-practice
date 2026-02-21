"""
Problem Statement:
Given a signed 32-bit integer x, return x with its digits reversed. Input: 123 → Output: 321. Input: -123 → Output: -321. Input: 120 → Output: 21 (no leading zeros). Solve this using math only — no string conversion allowed.

Intuition:
The key mathematical insight is that you can extract digits from right to left using modulo (% 10) and build the reversed number by multiplying the accumulator by 10 before adding each digit. This is the digit extraction pattern: repeatedly divide by 10 (integer division) to strip the last digit, and use modulo 10 to capture it.

Approach:
1. Handle the sign separately: store the sign, then work with the absolute value.
2. Initialize reverse = 0.
3. While x > 0: extract the last digit with digit = x % 10, then build reverse = reverse * 10 + digit, then remove the last digit with x = x // 10.
4. Multiply the result by the stored sign and return.

Time Complexity:
O(log N) where N is the value of the number — the number of digits is proportional to log10(N)

Space Complexity:
O(1) — only a few integer variables are used

Common Mistakes:
- Converting to string and reversing (str(x)[::-1]) — this bypasses the mathematical technique the problem is testing
- Forgetting to handle the sign: -123 reversed as 321- is invalid
- Not handling trailing zeros in the input: 120 should become 21, not 021
- In languages with fixed integer sizes, not checking for 32-bit overflow after reversal

Final Thoughts:
The digit extraction pattern (% 10 to get, // 10 to remove) is fundamental. You will use it again in palindrome number checking, Armstrong numbers, and many other number theory problems. Master this loop pattern here.
"""

# Reverse a Number (The Math Way)
# Extracting digits without string conversion
# The Problem: Reverse IntegerGiven a signed 32-bit integer x, return x with its digits reversed.
# Input: 123 -> Output: 321
# Input: -123 -> Output: -321
# Input: 120 -> Output: 21 (No leading zeros)

def reverse_integer(x):
    if x == 0:
        return 0
    
    if x > 0:
        sign = 1
    else:
        sign = -1
        x = -x
    
    reverse = 0
    while x > 0:
        digit = x % 10
        reverse = reverse * 10 + digit
        x = x // 10
    
    return sign * reverse

print(reverse_integer(123))
print(reverse_integer(-123))
print(reverse_integer(120))