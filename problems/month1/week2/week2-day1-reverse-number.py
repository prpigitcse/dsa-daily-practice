"""
Problem Statement:
Given an integer, reverse its digits. For example, 1234 becomes 4321, and -1234 becomes -4321. Note: If the reversed number would overflow a 32-bit integer range $[-2^{31}, 2^{31}-1]$, return 0.

Intuition:
Reversing digits mathematically uses the modular operator to extract the last digit and integer division to remove it: $\text{last\_digit} = n \bmod 10$, then $n = \lfloor n / 10 \rfloor$. The extracted digit is appended to the reversed number by shifting left: $\text{result} = \text{result} \times 10 + \text{last\_digit}$.

Approach:
1. Handle the sign: store `is_negative = n < 0` and work with `abs(n)`.
2. While `n > 0`, extract the last digit via `n % 10` and append to result via `result = result * 10 + digit`.
3. Remove the last digit with `n = n // 10`.
4. After the loop, reapply the sign if needed.
5. Check overflow: if the result is outside $[-2^{31}, 2^{31}-1]$, return 0.

Time Complexity:
$O(\log_{10} N)$ — the number of iterations equals the number of digits in $N$

Space Complexity:
$O(1)$ — only a few integer variables

Common Mistakes:
- Using Python string conversion (`str(n)[::-1]`) — correct but doesn't handle the overflow check naturally
- Not preserving the sign: using `abs()` but forgetting to reapply negative sign
- Integer overflow: Python has unlimited integers, so you must manually check the 32-bit bounds

Code Explanation:
- `is_negative = n < 0`: Captures the sign before taking absolute value.
- `n = abs(n)`: Work with a positive number to simplify the math.
- `result = 0`: Accumulator for the reversed number.
- `while n > 0`: Continues as long as there are digits remaining.
- `digit = n % 10`: Extracts the last digit using modulo (e.g., `1234 % 10 = 4`).
- `result = result * 10 + digit`: Shifts result left by one decimal place, then appends the new digit.
- `n = n // 10`: Removes the last digit using integer division (e.g., `1234 // 10 = 123`).
- `if is_negative: result = -result`: Reapplies the negative sign.
- `if result < -2**31 or result > 2**31 - 1: return 0`: 32-bit overflow check.

Final Thoughts:
This problem teaches digit-by-digit decomposition using modulo and integer division — a pattern that reappears in Armstrong number checks, palindrome number checks, and digit sum calculations.
"""

# Week 2 Day 1: Reverse a Number
# Given an integer, reverse its digits. e.g. 1234 -> 4321.

def reverse_number(n):
    is_negative = n < 0
    n = abs(n)
    result = 0
    while n > 0:
        digit = n % 10
        result = result * 10 + digit
        n = n // 10
    if is_negative:
        result = -result
    if result < -2**31 or result > 2**31 - 1:
        return 0
    return result

print(reverse_number(1234))   # 4321
print(reverse_number(-1234))  # -4321