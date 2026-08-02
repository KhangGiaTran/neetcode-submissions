class Solution:

    def encode(self, strs: List[str]) -> str:
        # length>...
        encoded = ""
        for s in strs:
            encoded += str(len(s)) + ">" + s
        return encoded

    def decode(self, s: str) -> List[str]:
        decoded = []

        prev = ""
        i = 0
        while i < len(s):
            c = s[i]
            if c == ">":
                length = int(prev)
                
                decoded.append(s[i + 1 : i + length + 1])

                i = i + length + 1
                prev = ""
            else:
                prev += c
                i+=1

        return decoded