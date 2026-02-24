"""
Pattern:
Basic Math

Problem Statement:
Given an integer $N$, determine if it is a prime number. A prime is a number greater than 1 that has no divisors other than 1 and itself. Input: 29 → True. Input: 30 → False.

Intuition:
If $N$ has a factor $f > \sqrt{N}$, then $N/f < \sqrt{N}$ is also a factor — so the smaller factor would already have been found. This means we only need to test divisors up to $\sqrt{N}$, reducing the check from $O(N)$ to $O(\sqrt{N})$.

Approach:
1. Return False for $N \leq 1$ (by definition, not prime).
2. Return True for $N = 2$ (only even prime).
3. Return False for even $N > 2$.
4. Loop odd divisors from 3 to $\lfloor \sqrt{N} \rfloor + 1$ (step 2).
5. If any divisor evenly divides $N$, return False.
6. Otherwise return True.

Time Complexity:
$O(\sqrt{N})$ — we only check up to the square root

Space Complexity:
$O(1)$ — no extra space

Common Mistakes:
- Checking all $N$ divisors instead of just up to $\sqrt{N}$
- Forgetting that 2 is prime and even (the only even prime)
- Using `range(2, N)` instead of `range(3, int(N**0.5)+1, 2)`

Code Explanation:
- `if n <= 1: return False`: 0 and 1 are not prime by definition.
- `if n == 2: return True`: 2 is the only even prime; must be handled before the even check.
- `if n % 2 == 0: return False`: All other even numbers are not prime (eliminates ~half the candidates immediately).
- `for i in range(3, int(n**0.5) + 1, 2)`: Starts at 3, increments by 2 (odd numbers only, since even have been eliminated), stops at $\lfloor \sqrt{N} \rfloor$ (inclusive due to `+1`).
- `int(n**0.5)`: Computes $\sqrt{N}$ as a float and casts to int, giving the floor value.
- `if n % i == 0: return False`: Found a divisor; not prime.
- `return True`: No divisors found in range; it's prime.

Final Thoughts:
The $\sqrt{N}$ optimization is one of the most important tricks in number theory problems. This exact technique is used in the Sieve of Eratosthenes (Day 6) and prime factorization (Day 7).
"""

# Week 2 Day 5: Prime Check
# Given an integer N, determine if it is a prime number.

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

print(is_prime(29))  # True
print(is_prime(30))  # False
print(is_prime(2))   # True
print(is_prime(1))   # False