"""
Convert a non-negative integer to its english words representation. Given input is guaranteed to be less than 231 - 1.

Example 1:

Input: 123
Output: "One Hundred Twenty Three"
Example 2:

Input: 12345
Output: "Twelve Thousand Three Hundred Forty Five"
Example 3:

Input: 1234567
Output: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
Example 4:

Input: 1234567891
Output: "One Billion Two Hundred Thirty Four Million Five Hundred Sixty Seven Thousand Eight Hundred Ninety One"
"""
class Solution:
    def numberToWords(self, num: int) -> str:
        lvl1 = "Zero One Two Three Four Five Six Seven Eight Nine Ten Eleven Twelve Thirteen Fourteen Fifteen Sixteen Seventeen Eighteen Nineteen".split(" ")
        lvl2 = "Twenty Thirty Forty Fifty Sixty Seventy Eighty Ninety".split(" ")
        lvl3 = "Hundred"
        lvl4 = "Thousand Million Billion".split(" ")
        current = num
        res = []
        commas = 0
        while current >0:
            n = current % 1000
            current = current // 1000
            words=[]
            if n > 99:
                words.append(lvl1[n//100])
                words.append(lvl3)
                n = n% 100
            if n > 19:
                words.append(lvl2[n//10-2])
                n = n%10
            if n >0:
                words.append(lvl1[n])
            if len(words)>0:
                if commas >0:
                    words.append(lvl4[commas-1])
                res.append(" ".join(words))
            commas+=1
        if len(res):
            res = reversed(res)
            return ' '.join(res)
        return "Zero"
