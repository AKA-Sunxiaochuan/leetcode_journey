"""
20. Valid Parentheses
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
Example 4:

Input: s = "([)]"
Output: false
Example 5:

Input: s = "{[]}"
Output: true
 

Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.

https://leetcode-cn.com/problems/valid-parentheses
"""


class Solution:
    def isValid(self, s):
        dict_ = {")": "(", "]": "[", "}": "{"}

        lst = list(s)
        stack_ = [lst[0]]

        for i in lst[1:]:
            stack_.append(i)

            if len(stack_) > 1:
                if i == ")" or i == "]" or i == "}":
                    if i in dict_:
                        j = dict_[i]

                    if j == stack_[-2]:
                        stack_.pop()
                        stack_.pop()

        if len(stack_) == 0:
            return True
        else:
            return False

