"""
Problem Statement:
Write a function gcd(a, b) that finds the Greatest Common Divisor — the largest positive integer that divides both a and b without a remainder. For example, gcd(48, 18) = 6. You must use the Euclidean Algorithm, not a brute-force loop.

Intuition:
The Euclidean Algorithm is based on a mathematical property: gcd(a, b) = gcd(b, a % b). By repeatedly replacing the larger number with the remainder of dividing the two, the pair eventually reduces to (gcd, 0). This is dramatically faster than checking every number from 1 to min(a, b).

Approach:
1. While b is not 0, replace (a, b) with (b, a % b).
2. When b becomes 0, a holds the GCD.
3. The order of a and b doesn't matter — the algorithm self-corrects after one iteration.

Time Complexity:
O(log(min(a, b))) — each step reduces the problem size by at least half

Space Complexity:
O(1) — only two variables are swapped in-place

Common Mistakes:
- Using a brute-force loop from min(a, b) down to 1, which is O(N) and too slow for large inputs
- Getting the swap wrong: it must be a, b = b, a % b (not a % b, b)
- Not handling the case where one input is 0: gcd(0, n) = n and gcd(n, 0) = n
- Confusing GCD with LCM (Least Common Multiple): LCM(a, b) = (a * b) / GCD(a, b)

Final Thoughts:
The Euclidean Algorithm is over 2,300 years old and is one of the most elegant algorithms in computer science. Its logarithmic time complexity makes it practical even for numbers with hundreds of digits. This is a foundational algorithm used in cryptography (RSA), fraction simplification, and many number theory problems.
"""

# The Problem: Greatest Common Divisor (GCD)
# Write a function gcd(a, b) that finds the largest positive integer that divides both numbers without a remainder.

# Input: 48, 18

# Output: 6

# Explanation:

# Divisors of 18: 1, 2, 3, 6, 9, 18

# Divisors of 48: 1, 2, 3, 4, 6, 8, 12, 16, 24, 48

# Largest common one is 6.

# Constraint:
# You must use the Euclidean Algorithm. Do not use a loop that counts down from min(a, b)—that is O(N) and too slow for large inputs. The Euclidean approach is O(logN).

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

print(gcd(48, 18))
print(gcd(18, 48))
print(gcd(0, 18))
print(gcd(18, 0))
print(gcd(3, 7))
print(gcd(7, 3))
