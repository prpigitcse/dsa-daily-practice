"""
Problem Statement:
Given an integer n, return the count of prime numbers that are strictly less than n. Use the Sieve of Eratosthenes — do not simply loop and call an is_prime function for each number. Input: 10 → 4 (primes: 2, 3, 5, 7). Input: 0 → 0. Input: 1 → 0.

Intuition:
Instead of checking each number individually for primality (O(N√N) total), the Sieve of Eratosthenes eliminates composites in bulk. Start by assuming all numbers are prime. For each prime found, mark all its multiples as composite. What remains are the primes. This is a "mark and sweep" approach.

Approach:
1. If n < 2, return 0.
2. Create a boolean array of size n, initialized to True (all assumed prime).
3. Mark indices 0 and 1 as False (not prime).
4. For each number i from 2 to √n: if primes[i] is True, mark all multiples of i (starting from i*i) as False.
5. Count the True values remaining in the array.

Time Complexity:
O(N log log N) — this is the proven time complexity of the Sieve of Eratosthenes, nearly linear

Space Complexity:
O(N) — the boolean array stores one entry per number up to n

Common Mistakes:
- Starting the inner loop from 2*i instead of i*i (all multiples less than i*i have already been marked by smaller primes)
- Using the range as inclusive of n (the problem asks for primes strictly less than n)
- Calling is_prime(i) inside a loop — this defeats the purpose of the sieve
- Not marking 0 and 1 as non-prime

Final Thoughts:
The Sieve of Eratosthenes is one of the oldest algorithms in mathematics (circa 200 BC). It demonstrates a powerful algorithmic theme: precomputation. Instead of answering each query independently, compute all answers at once. This trade-off of space for time is a recurring pattern in DSA. The sieve can find all primes below 10 million in under a second.
"""

# The Problem: Count Primes
# Given an integer n, return the number of prime numbers that are strictly less than n.
# Input: 10 Output: 4 (Primes are 2, 3, 5, 7)
# Input: 0  Output: 0
# Input: 1  Output: 0
# Constraint:You must use the Sieve of Eratosthenes. Do not just loop and call your is_prime function.

def count_primes(n):
    if n < 2:
        return 0
    primes = [True] * n
    primes[0] = primes[1] = False

    for i in range(2, int(n**0.5) + 1):
        if primes[i]:
            for multiple in range(i*i, n, i):
                primes[multiple] = False

    return sum(primes)

print(count_primes(10))
print(count_primes(0))
print(count_primes(1))
print(count_primes(2))
print(count_primes(20))
print(count_primes(100))
print(count_primes(1000))