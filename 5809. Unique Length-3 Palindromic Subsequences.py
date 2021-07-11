import bisect
class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        info = {  ch:[-1]  for ch in "abcdefghijklmnopqrstuvwxyz"}
        for i,c in enumerate(s):
            info[c].append(i)
        for ch in "abcdefghijklmnopqrstuvwxyz":
            info[ch].append(999999)
        ans=0
        for i,c in enumerate(s):
            firstLoc=info[c][1]
            lastLoc=info[c][-2]
            kinds=0
            if (i == firstLoc):
                for letter  in "abcdefghijklmnopqrstuvwxyz":
                    tmp = firstLoc + 1 if c == letter else firstLoc
                    j=bisect.bisect_left(info[letter],tmp)
                    if info[letter][j] < lastLoc:
                        kinds+=1
                ans+=kinds
        return ans
    
sln=Solution()
assert 3==sln.countPalindromicSubsequence(s = "aabca")
assert 4==sln.countPalindromicSubsequence( s = "bbcbaba")
assert 0==sln.countPalindromicSubsequence( s = "adc")

