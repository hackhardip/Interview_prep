class Solution:
    def customSortString(self, S: str, T: str) -> str:
        counts = {}
        for t in T:
            if t in counts:
                counts[t] += 1
            else:
                counts[t] = 1
        
        output = ""
        for s in S:
            if s in counts:
                output += s * counts[s] 
                counts[s] = 0
            
        for t in T:
            if counts[t] > 0:
                output += t
                
        return output
