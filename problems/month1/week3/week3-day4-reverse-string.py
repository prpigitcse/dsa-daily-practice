"""
Problem Statement:
Write a recursive function reverse_string(s) that returns the reversed string. Input: "hello" → Output: "olleh". Input: "abc" → Output: "cba". You must use recursion — no loops or slicing tricks like [::-1].

Intuition:
The recursive insight is: reversing a string means putting the first character at the end, after reversing the rest. Alternatively, you can recurse to the end of the string and build the result on the way back. The base case is reaching the end of the string (index == len). Each recursive call processes one character deeper, and concatenation happens on the way back up.

Approach:
1. Use an index parameter (default 0) to track position.
2. Base case: if index == len(str), return an empty string "".
3. Recursive case: return reverse_string(str, index + 1) + str[index].
4. This recurses to the end first, then appends characters in reverse order as the stack unwinds.

Time Complexity:
O(N) recursive calls, but O(N^2) total due to string concatenation creating new strings at each step

Space Complexity:
O(N) for the recursion call stack

Common Mistakes:
- Using [::-1] slicing — this works but defeats the purpose of learning recursion
- Not understanding how the concatenation order creates the reversal (the deepest character is added first)
- String concatenation in Python creates new strings, making this O(N^2) — for production, use a list and join
- Forgetting the base case, leading to infinite recursion

Final Thoughts:
This problem shows how recursion can replace iteration for string processing. The pattern of "recurse to the end, then build on the way back" is important — it appears in tree traversals and many other recursive algorithms. Understanding the call stack unwinding process is key to grasping how this reversal works.
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