class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x = str(x)
        x = list(x)
        base_x = x[:]
        list_x = []
        for i in range(len(x)):
            list_x.append(x.pop())
        if base_x == list_x:
            return True
        else: 
            return False