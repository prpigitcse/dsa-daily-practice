"""
Pattern:
Recursion

Problem Statement:
Write a recursive function `reverse_string(s)` that returns the reversed string. Input: "hello" → Output: "olleh". Input: "abc" → Output: "cba". You must use recursion — no loops or `[::-1]`.

Intuition:
Reversing recursively: recurse to the end of the string, then append characters in reverse order as the stack unwinds. The $i$-th call places `s[i]` after all characters from index $i+1$ onward.

Approach:
1. Use an index parameter (default 0) to track position.
2. Base case: if `index == len(str)`, return `""`.
3. Recursive case: return `reverse_string(str, index + 1) + str[index]`.
4. This recurses to the end first, then appends characters in reverse on the way back.

Time Complexity:
$O(N)$ recursive calls, but $O(N^2)$ total due to string concatenation creating a new string at each level

Space Complexity:
$O(N)$ for the recursion call stack

Common Mistakes:
- Using `[::-1]` slicing — correct but defeats the purpose of learning recursion
- Not understanding how the concatenation order creates the reversal
- String concatenation in Python creates new strings — $O(N^2)$ total; use a list + join for production
- Forgetting the base case, causing infinite recursion

Code Explanation:
- `def reverse_string(str, index=0)`: Accepts the string and a current `index`, defaulting to 0 so callers don't need to pass it.
- `if index == len(str): return ""`: **Base case**: when `index` reaches the end of the string, return an empty string to start unwinding.
- `return reverse_string(str, index+1) + str[index]`: **Recursive case**: first recurse deeper (`index+1`), then concatenate `str[index]` **after** the result of the deeper call.
- The key to understanding the reversal is that `str[index]` is appended **after** the deeper call result. So for `"abc"`:
    - `reverse_string("abc", 0)` = `reverse_string("abc", 1)` + `"a"`
    - `reverse_string("abc", 1)` = `reverse_string("abc", 2)` + `"b"`
    - `reverse_string("abc", 2)` = `reverse_string("abc", 3)` + `"c"`
    - `reverse_string("abc", 3)` = `""`
    - Unwinding: `""` + `"c"` + `"b"` + `"a"` = `"cba"`.

Final Thoughts:
The pattern of "recurse to the end, then build on the way back" appears in tree traversals and many recursive algorithms. Understanding the call stack unwinding is key to grasping how this reversal works.
"""

# The Problem: Reverse a String (Recursive)
# Write a function reverse_string(s) that returns the reversed string.
# Input: "hello" -> Output: "olleh"
# Input: "abc" -> Output: "cba"
# Constraint: You must use Recursion. No loops or [::-1].

def reverse_string(str, index=0):
    if index == len(str):
        return ""
    
    return reverse_string(str, index+1) + str[index]

print(reverse_string("abc"))
print(reverse_string("hello"))