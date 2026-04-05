class Solution:

    def encode(self, strs: List[str]) -> str:
        output = ""
        for strc in strs:
            output += f"{len(strc)}#{strc}"
        print(output)
        return output

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length_w = int(s[i:j])
            i = j+1
            j = i + length_w
            result.append(s[i:j])
            i = j
        return result