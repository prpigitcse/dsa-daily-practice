"""
Problem Statement:
A number is an Armstrong number (narcissistic number) if it equals the sum of its own digits each raised to the power of the number of digits. For example, $153 = 1^3 + 5^3 + 3^3$. Write a function that returns True if a number is an Armstrong number.

Intuition:
For a number with $d = \lfloor \log_{10} N \rfloor + 1$ digits, it is Armstrong if $N = \sum_{i} d_i^d$ where $d_i$ are its digits. The key insight is that you need the total digit count **before** summing — compute it once, then extract each digit using the modulo loop from Day 1.

Approach:
1. Count the number of digits: `d = len(str(n))` or using $\lfloor \log_{10} N \rfloor + 1$.
2. Extract digits one by one using `n % 10` and `n // 10`.
3. For each digit, raise it to the power `d` and add to a running sum.
4. Compare the sum to the original number.

Time Complexity:
$O(\log_{10} N)$ — proportional to the number of digits

Space Complexity:
$O(1)$ — only integer variables

Common Mistakes:
- Computing the number of digits inside the loop (recalculated wrongly as digits are removed)
- Using `n % 10` after modifying `n` without saving the original — always save `original = n`
- Only testing single-digit numbers (1–9 are trivially Armstrong); test 153, 370, 371, 407

Code Explanation:
- `original = n`: Save the input so we can compare at the end (the loop will consume `n`).
- `num_digits = len(str(n))`: Count digits by converting to string; `len("153") == 3`.
- `armstrong_sum = 0`: Running total of digit^power values.
- `while n > 0`: Extract digits one at a time.
- `digit = n % 10`: Last digit of the remaining number.
- `armstrong_sum += digit ** num_digits`: Raise to the power of total digits and accumulate.
- `n = n // 10`: Remove the last digit.
- `return armstrong_sum == original`: True if the digit-power sum equals the original number.

Final Thoughts:
Armstrong numbers combine two patterns you've already seen: digit extraction (Day 1, Day 2) and exponentiation. The important lesson here is to compute `num_digits` **once before the loop**, not inside it.
"""

# Week 2 Day 3: Armstrong Number
# A number is an Armstrong number if it equals the sum of its digits each raised to the power of the number of digits.

def is_armstrong(n):
    original = n
    num_digits = len(str(n))
    armstrong_sum = 0
    while n > 0:
        digit = n % 10
        armstrong_sum += digit ** num_digits
        n = n // 10
    return armstrong_sum == original

print(is_armstrong(153))  # True
print(is_armstrong(370))  # True
print(is_armstrong(123))  # False