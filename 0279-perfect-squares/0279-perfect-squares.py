class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        arr = [10001]*10001

        for i in range(1, 101):
            arr[i*i] = 1

        for i in range(1, n+1):
            if arr[i] == 1:
                continue

            for j in range(1, int(math.sqrt(i))+1):
                arr[i] = min(arr[i], arr[i-j*j]+1)
            
        return arr[n]