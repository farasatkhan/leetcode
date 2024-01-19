from typing import List
from collections import defaultdict

class Solution:
    def groupAnagram(self, str: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)
        for word in str:
            hashmap[tuple(sorted(word))].append(word)
        return hashmap.values()

if __name__ == "__main__":
    s = Solution()
    print(s.groupAnagram(["eat", "tea", "tan", "ate", "nat", "bat"]))