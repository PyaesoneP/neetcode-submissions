from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = defaultdict(list)
        for st in strs:
            sorted_st = "".join(sorted(st))
            seen[sorted_st].append(st)

        return list(seen.values())
