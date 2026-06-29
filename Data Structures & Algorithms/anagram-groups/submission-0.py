class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {}
        for st in strs:
            sorted_st = "".join(sorted(st))
            if sorted_st in seen:
                seen[sorted_st].append(st)
            else:
                seen.setdefault(sorted_st, []).append(st)

        return list(seen.values())
