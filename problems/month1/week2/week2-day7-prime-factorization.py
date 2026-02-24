"""
Pattern:
Basic Math

Problem Statement:
Given an integer $N$, return its prime factorization as a list of prime factors. For example, $12 = 2 \times 2 \times 3$, so the output is [2, 2, 3]. $N = 1$ returns an empty list.

Intuition:
Repeatedly divide $N$ by the smallest possible prime factor. Start with 2 (to handle all even factors), then check only odd numbers from 3 to $\sqrt{N}$. If $N > 1$ after the loop, the remaining value is itself a prime factor (the largest one).

Approach:
1. Initialize an empty list `factors`.
2. While $N$ is divisible by 2, append 2 and divide $N$ by 2.
3. For odd divisors $i = 3, 5, 7, \ldots$ up to $\sqrt{N}$: while $N$ is divisible by $i$, append $i$ and divide.
4. If $N > 1$ after the loop, $N$ is a prime — append it.

Time Complexity:
$O(\sqrt{N})$ for the trial division loop

Space Complexity:
$O(1)$ — constant extra space (excluding the output list)

Common Mistakes:
- Only dividing by each factor once instead of looping (misses repeated factors, e.g., `12 = 2 × 2 × 3`)
- Not handling the "remaining prime" case after the loop — e.g., `14 = 2 × 7`; after dividing by 2, `n = 7 > 1`, so 7 must be appended
- Checking only up to $\sqrt{\text{original } N}$ instead of dynamically comparing to $i^2 \leq n$ (the latter is correct since $n$ shrinks)

Code Explanation:
- `factors = []`: List to collect all prime factors.
- `while n % 2 == 0`: Handle all factors of 2 first (the only even prime).
- `factors.append(2); n //= 2`: Append 2 and divide out all 2s.
- `i = 3`: Start checking odd divisors from 3.
- `while i * i <= n`: Loop while `i` could still be a factor; equivalent to `i <= sqrt(n)`.
- `while n % i == 0`: Divide out all occurrences of `i` (handles repeated factors like $8 = 2^3$).
- `factors.append(i); n //= i`: Append factor and shrink `n`.
- `i += 2`: Skip even numbers (already handled by the `%2` check).
- `if n > 1: factors.append(n)`: Any remaining value greater than 1 is a prime factor (couldn't be divided by anything up to its own $\sqrt{}$).

Final Thoughts:
Prime factorization underlies RSA encryption: factoring a large number $N = p \times q$ is computationally infeasible for huge primes, while multiplying them is easy. The "remaining prime" optimization after the loop is elegant — it's the key insight that keeps this solution correct and $O(\sqrt{N})$.
"""

# Week 2 Day 7: Prime Factorization
# Given an integer N, return its prime factorization as a list.

def prime_factorization(n):
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n //= 2
    i = 3
    while i * i <= n:
        while n % i == 0:
            factors.append(i)
            n //= i
        i += 2
    if n > 1:
        factors.append(n)
    return factors

print(prime_factorization(12))   # [2, 2, 3]
print(prime_factorization(100))  # [2, 2, 5, 5]
print(prime_factorization(97))   # [97] (prime)