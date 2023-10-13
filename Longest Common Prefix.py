def longestCommonPrefix(self, strs: List[str]) -> str:
        ans=''
        s=sorted(strs)
        l=s[0]
        r=s[-1]

        for i in range(min(len(l), len(r))):
            if l[i]!=r[i]:
                return ans
            ans+=l[i]
        return ans