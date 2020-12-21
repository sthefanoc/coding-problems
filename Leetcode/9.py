class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x<0:
            return False
        x = str(x)
        size = len(x)
        print(size)
        if size == 1:
          return True
        k=0
        for i in range(size // 2):
          print(x[k], x[size-1])
          if not (x[k] == x[size-1]):
            return False
            print(x[k] == x[size-1])
          k += 1
          size -= 1
        return True
