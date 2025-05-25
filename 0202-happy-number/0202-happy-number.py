class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        arr = defaultdict(int)
        arr[n] = 1

        while True:
            total = 0
            while n != 0:
                cur = n % 10
                total += cur * cur
                n = n // 10

            n = total
            if n == 1:
                return True
            if n in arr:
                return False

            arr[n] = 1

        