class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        fib1 = 1
        fib2 = 1
        current = 2
        for i in range(n-2):
            fib2 = fib1
            fib1 = current
            current = fib1 + fib2
        return current
