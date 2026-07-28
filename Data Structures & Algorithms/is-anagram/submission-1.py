class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        cnt = {}
        for ch in s:
            if ch not in cnt:
                cnt[ch] = 0
            cnt[ch] += 1

        for ch in t:
            if ch not in cnt:
                return False
            cnt[ch] -= 1
            if cnt[ch] < 0:
                return False
        return True