#
# @lc app=leetcode id=150 lang=python3
#
# [150] Evaluate Reverse Polish Notation
#
import operator
# @lc code=start
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = {
            "+": operator.add,
            "-": operator.sub,
            "*": operator.mul,
            "/": operator.truediv,
        }
        stack = []
        for token in tokens:
            if token in operators:
                stack.append(int(operators[token](stack.pop(-2), stack.pop(-1))))
            else:
                stack.append(int(token))
        return stack[0]
# @lc code=end