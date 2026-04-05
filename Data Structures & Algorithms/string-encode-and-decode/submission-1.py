class Solution:

    def encode(self, strs: List[str]) -> str:
        output = ""
        for strc in strs:
            output += f"{len(strc)}#{strc}"
        print(output)
        return output

    def decode(self, s: str) -> List[str]:
        def word_recursion(idx, s, words):
            if idx >= len(s):
                return words

            # read the length
            len_curr = ""
            while s[idx] != "#":
                len_curr += s[idx]
                idx += 1
            idx += 1  # skip '#'
            length = int(len_curr)

            # append the word
            words.append(s[idx:idx+length])

            # recurse for the next word
            return word_recursion(idx+length, s, words)
        return word_recursion(0, s, [])

        

            