class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        limit = 2**31
        if s == '':
          return 0
        while '  ' in s:
          s = s.replace('  ', ' ')
        x = s.split(' ')[0] if len(s.split(' ')[0])>0 else s.split(' ')[1]
        for j,c in enumerate(x):
          if c.isalpha() or (c in ['+','-'] and j>0):
            x = x[:j]
            break
        try:
          x = int(round(float(x),0))
        except:
          x = 0
        if x < limit and x > -limit:
          return x
        elif x >= limit:
          return limit -1
        else:
          return -limit
