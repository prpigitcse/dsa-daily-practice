"""
Problem Statement:
Given a positive integer n, return a list of all its prime factors (with repetition). Input: 12 → [2, 2, 3] (because 2×2×3 = 12). Input: 315 → [3, 3, 5, 7]. Input: 13 → [13] (prime number). The output should be sorted in ascending order.

Intuition:
The approach mirrors the prime check optimization: only test divisors up to √n. First, extract all factors of 2 (the only even prime). Then test odd numbers from 3 upward up to √n. If after this process n > 1, whatever remains must itself be a prime factor. The factors naturally come out sorted because we test small divisors first.

Approach:
1. Extract all factors of 2: while n is even, append 2 and divide n by 2.
2. Start d = 3. While d * d ≤ n, check if d divides n. If yes, append d and divide. Otherwise increment d by 2 (skip even numbers).
3. If n > 1 after the loop, n itself is a prime factor — append it.
4. Return the list of factors.

Time Complexity:
O(√N) — we only check divisors up to the square root

Space Complexity:
O(log N) — the number of prime factors is at most log2(N) (when n is a power of 2)

Common Mistakes:
- Iterating up to n instead of √n, making it O(N) which is too slow for large inputs
- Forgetting the final check if n > 1 (this misses the largest prime factor)
- Not handling the factor 2 separately, then trying to skip even numbers (leads to missing 2 as a factor)
- Using a primality test for each potential factor — unnecessary since non-primes will never divide n after their prime components have been extracted

Final Thoughts:
Prime factorization ties together the √N optimization from is_prime and the digit extraction loop pattern. The elegance of this algorithm is that you don't need a list of primes — by dividing out each factor completely before moving on, non-prime candidates automatically become irrelevant. This is used in cryptography, simplifying fractions, and computing LCM.
"""

# The Problem: Prime Factorization
# Given a positive integer n, return a list of all its prime factors.
# Input: 12 → Output: [2, 2, 3] (2×2×3=12)
# Input: 315 → Output: [3, 3, 5, 7]
# Input: 13 → Output: [13] (It's a prime number)
# Constraints:
# Time Complexity must be O(sqrt(N)). You cannot iterate up to n.
# The output list should be sorted (naturally happens if you solve it correctly).

def get_prime_factors(n):
    prime_factors = []
    d = 2

    while n > 0 and n % 2 == 0:
        prime_factors.append(2)
        n = n // 2

    d = 3
    while d * d <= n:
        while n % d == 0:
            prime_factors.append(d)
            n = n // d
        d += 2
    
    if n > 1:
        prime_factors.append(n)
    
    return prime_factors
            

print(get_prime_factors(12))
print(get_prime_factors(315))
print(get_prime_factors(13))
print(get_prime_factors(9))