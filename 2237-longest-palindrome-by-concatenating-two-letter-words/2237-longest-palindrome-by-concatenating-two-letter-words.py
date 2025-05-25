class Solution(object):
    def longestPalindrome(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        palin = {}
        same = {}

        ans = 0
        for w in words:
            if w[1] == w[0]:
                if w not in same:
                    same[w] = 1
                else:
                    same[w] += 1

            if w[1]+w[0] in palin:
                if palin[w[1]+w[0]] > 1:
                    palin[w[1]+w[0]] -= 1
                else:
                    palin.pop(w[1]+w[0], None)
                # print(w[1]+w[0])
                # print(palin)
                ans += 4
            else:
                if w in palin:
                    palin[w] += 1
                else:
                    palin[w] = 1

            # if w not in palin:
            #     if w[1]+w[0] in palin:
            #         if palin[w]



            #     if w[1]+w[0] not in palin:
            #         palin[w] = 1
            #     else:
            #         palin[w[1]+w[0]] += 1
            # else:
            #     palin[w] += 1
        
        print(palin)
        print(same)

        # ans = 0
        for i, v in same.items():
            if v % 2 == 1:
                ans += 2
                break
        
        # for i, v in palin.items():
        #     if v % 2 == 0:
        #         ans += v * 2

        return ans
        