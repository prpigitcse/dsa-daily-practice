"""
Pattern:
Basic Math

Problem Statement:
Given an integer $N$, return a list of all prime numbers from 2 to $N$ (inclusive) using the Sieve of Eratosthenes algorithm. For example, $N = 30$ → [2, 3, 5, 7, 11, 13, 17, 19, 23, 29].

Intuition:
Instead of checking each number individually (which takes $O(\sqrt{N})$ per number), the Sieve marks all multiples of each prime as composite in bulk. Start from the smallest prime (2), mark all its multiples as not prime, then move to the next unmarked number, and repeat. The outer loop only runs up to $\sqrt{N}$ because any composite number's smallest prime factor must be $\leq \sqrt{N}$.

Approach:
1. Create a boolean array `is_prime` of size $N+1$, initialized to True.
2. Set `is_prime[0] = is_prime[1] = False`.
3. For each $i$ from 2 to $\lfloor \sqrt{N} \rfloor$: if `is_prime[i]` is True, mark all multiples starting at $i^2$ as False.
4. Collect all indices where `is_prime[i]` is still True.

Time Complexity:
$O(N \log \log N)$ — from the harmonic series over primes

Space Complexity:
$O(N)$ — for the boolean sieve array

Common Mistakes:
- Starting the inner loop from $2i$ instead of $i^2$ — the smaller multiples were already marked by earlier primes
- Not marking 0 and 1 as non-prime before collecting results
- Using a list of integers instead of a boolean array — wastes memory

Code Explanation:
- `is_prime = [True] * (n + 1)`: Creates a list of $N+1$ boolean values, all initially True. Index $i$ represents whether $i$ is prime.
- `is_prime[0] = is_prime[1] = False`: 0 and 1 are not prime by definition.
- `for i in range(2, int(n**0.5) + 1)`: Outer loop up to $\sqrt{N}$ (composites are guaranteed to have a factor $\leq \sqrt{N}$).
- `if is_prime[i]`: Only process numbers that haven't been marked composite yet.
- `for j in range(i * i, n + 1, i)`: Mark multiples of `i` starting at $i^2$ (smaller multiples were already sieved by earlier primes). Step size is `i`.
- `is_prime[j] = False`: Mark the composite number.
- `return [i for i in range(2, n + 1) if is_prime[i]]`: Collect all indices still marked True.

Final Thoughts:
The Sieve of Eratosthenes is the gold standard for generating all primes up to $N$. Understanding why the inner loop starts at $i^2$ (not $2i$) and why the outer loop only goes to $\sqrt{N}$ is key to grasping its efficiency.
"""

# Week 2 Day 6: The Sieve of Eratosthenes
# Given an integer N, return all prime numbers from 2 to N.

def sieve_of_eratosthenes(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = False
    return [i for i in range(2, n + 1) if is_prime[i]]

print(sieve_of_eratosthenes(30))