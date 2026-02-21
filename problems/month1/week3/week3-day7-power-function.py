"""
Problem Statement:
Write a recursive function power(x, n) that calculates x raised to the power n. Input: x = 2, n = 10 → Output: 1024. Input: x = 3, n = 3 → Output: 27. You must use recursion and cannot use the ** operator. Naive multiplication (x * x * x... n times) is O(N) — you must achieve O(log N).

Intuition:
The key insight is "exponentiation by squaring": x^n = (x^(n/2))^2 when n is even. This halves the problem at each step, achieving O(log N). For odd n, we extract one factor: x^n = x × (x^(n/2))^2. This is the same halving principle as binary search, applied to computation.

Approach:
1. Base case: if exp == 0, return 1 (anything to the power 0 is 1).
2. Recursively compute half = power(base, exp // 2).
3. If exp is even: return half * half.
4. If exp is odd: return base * half * half.
5. Validate: raise an error for negative exponents (for this basic version).

Time Complexity:
O(log N) where N is the exponent — we halve the exponent with each recursive call

Space Complexity:
O(log N) for the recursion stack

Common Mistakes:
- Using a simple loop (x * x * x... n times), which is O(N) — too slow for large exponents like n = 1,000,000
- Computing power(base, exp // 2) twice instead of storing the result in a variable (this turns O(log N) into O(N))
- Not handling exp = 0 as the base case
- Forgetting the odd exponent case: x^5 = x × (x^2)^2, not just (x^2)^2

Final Thoughts:
Fast exponentiation (also called binary exponentiation) is a cornerstone algorithm. It reduces 1,000,000 multiplications to about 20. This technique is used in modular exponentiation for cryptography (RSA), matrix exponentiation for Fibonacci, and competitive programming. The pattern of "compute half, then combine" is the essence of divide and conquer.
"""

# The Problem: Calculate x^n
# Write a recursive function power(x, n) that calculates x raised to the power of n.
# Input: x = 2, n = 10 Output: 1024
# Input: x = 3, n = 3 Output: 27
# Constraint:You must use Recursion.You cannot use the built-in ** operator for the whole problem, and you cannot just multiply x by itself n times (that would be O(N) time, which is too slow if n is 1,000,000).

def power(base, exp):
    if exp < 0:
        raise ValueError("Exponent must be >= 0")

    if exp == 0:
        return 1

    # Recursive call
    half = power(base, exp // 2)

    if exp % 2 == 0:
        return half * half
    else:
        return base * half * half


print(power(2, 10))   # 1024


