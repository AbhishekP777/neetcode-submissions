class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_strs = ''
        for i in strs :
            encoded_strs += f"{len(i)}@{i}"
        return encoded_strs

    def decode(self, s: str) -> List[str]:
        decoded_strs = []
        n = len(s)
        i = 0
        while i < n:
            for idx in range(i+1,n):
                if s[idx] == '@':
                    j = idx
                    break
            count = int(s[i:j])
            decoded_strs.append(s[(j+1):(j+count+1)])
            i = j+1+count
        return decoded_strs