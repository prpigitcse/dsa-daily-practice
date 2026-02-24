"""
Pattern:
Basic Math

Problem Statement:
Given two integers `a` and `b`, find their Greatest Common Divisor (GCD) using the Euclidean Algorithm. Also compute the Least Common Multiple (LCM) using $\text{LCM}(a, b) = \frac{a \times b}{\gcd(a, b)}$.

Intuition:
The Euclidean Algorithm is based on the identity $\gcd(a, b) = \gcd(b, a \bmod b)$. Repeatedly replacing the larger number with the remainder shrinks the problem rapidly ($O(\log \min(a, b))$ steps) compared to the naive approach of checking every divisor from 1 to $\min(a, b)$ ($O(N)$ steps).

Approach:
1. While `b != 0`, compute `a, b = b, a % b`.
2. When `b == 0`, `a` holds the GCD.
3. Compute LCM as `a * b // gcd(a, b)` using the formula $\text{LCM}(a, b) = \frac{a \times b}{\gcd(a, b)}$.
4. Use `//` (integer division) to avoid floating-point issues.

Time Complexity:
$O(\log \min(a, b))$ — the number of steps is bounded by the number of digits in the smaller input

Space Complexity:
$O(1)$ — only two variables updated in-place

Common Mistakes:
- Dividing after multiplying can cause integer overflow in languages with fixed-size integers; in Python this isn't an issue
- Forgetting that `gcd(0, n) = n` — the Euclidean stopping condition handles this correctly
- Using `a / b` (float division) instead of `a // b` in the LCM formula

Code Explanation:
- `def gcd(a, b)`: Takes two integers.
- `while b != 0`: Continues until the remainder becomes 0.
- `a, b = b, a % b`: Simultaneously: new `a` is old `b`, new `b` is `a mod b`. Python's tuple assignment makes the swap atomic (no temp variable needed).
- `return a`: When `b == 0`, `a` is the GCD.
- `def lcm(a, b)`: Calls `gcd` internally.
- `return a * b // gcd(a, b)`: Applies the LCM formula. `//` ensures integer output.

Final Thoughts:
The Euclidean Algorithm is one of the oldest algorithms in existence (~300 BCE). Its $O(\log N)$ performance comes from the Fibonacci numbers being the worst case — consecutive Fibonacci numbers require the maximum number of steps for any pair of that size.
"""

# Week 2 Day 4: Euclidean GCD Algorithm
# Given two integers a and b, find their GCD and LCM.

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

print(f"GCD(48, 18) = {gcd(48, 18)}")  # 6
print(f"LCM(48, 18) = {lcm(48, 18)}")  # 144
