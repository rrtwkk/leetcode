class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        parent = [i for i in range(26)]
        length = len(s1)
        for i in range(length):
            p1 = self.find(ord(s1[i])-ord('a'), parent)
            p2 = self.find(ord(s2[i])-ord('a'), parent)
            if (p1 != p2):
                parent[max(p1, p2)] = min(p1, p2)

        ans = ''.join(chr(self.find(ord(c)-ord('a'), parent)+ord('a'))
                      for c in baseStr)

        return ans

    def find(self, x, parent):
        if parent[x] == x:
            return x
        parent[x] = self.find(parent[x], parent)
        return parent[x]
