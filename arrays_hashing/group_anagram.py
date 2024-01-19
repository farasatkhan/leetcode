from typing import List
from collections import defaultdict

class Solution:
    def groupAnagram(self, str: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)

        for word in str:
            count = [0] * 26
            for character in word:
                count[ord(character) - ord("a")] += 1
            hashmap[tuple(count)].append(word)
            
        return hashmap.values()

    

if __name__ == "__main__":
    s = Solution()
    print(s.groupAnagram(["eat", "tea", "tan", "ate", "nat", "bat"]))