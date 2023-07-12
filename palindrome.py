class Solution:
    # Write code below to complete prompt
    def isPalindrome(self, s):
           if s.len() > 6:
                return False
           elif s[::-1] == s:
                return True
           else:
                return False
def main():
    tc1 = Solution()
    inpyt = input()
    # Write code below to complete prompt
    print(tc1.isPalindrome(inpyt))

if __name__ == "__main__":
    main()
