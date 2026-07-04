class Solution:
    def isPalindrome(self, s: str) -> bool:
        alpha_numeric = re.sub(r'[^A-Za-z0-9]', '', s).lower()
        for i in range(len(alpha_numeric) // 2):
            last_index = len(alpha_numeric) - 1 - i

            if alpha_numeric[i] != alpha_numeric[last_index]:
                return False

        return True