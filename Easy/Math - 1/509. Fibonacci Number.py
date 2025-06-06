class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :ret_type: int
        """
        # # Recursion (Basic Not ideal)
        # if n <= 1:
        #     return n
        # return self.fib(n-1)+self.fib(n-2)
        
        # Recursion with Memorization technique (Reduce memory stack overflow to some extent)
        # memo = {}
        # if n in memo:
        #     return memo[n]
        # if n <= 1:
        #     memo[n] = n
        # else:
        #     memo[n] = self.fib(n-1)+self.fib(n-2)
        # return memo[n]
        
        # Iterative way (Optimized Way)
        a,b = 0,1
        if n<=1:
            return n
        else:
            for i in range(2, n+1):
                a,b = b, a+b
            return b
        