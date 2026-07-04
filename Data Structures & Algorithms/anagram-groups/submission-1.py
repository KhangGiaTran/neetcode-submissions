class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)
        for string in strs:
            count = [0] * 26
            # build local map
            for char in string:
                count[ord(char) - ord('a')] += 1

            # get signature
            hashcode = tuple(count)
            hashmap[hashcode].append(string)

        return list(hashmap.values())