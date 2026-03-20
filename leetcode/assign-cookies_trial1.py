class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """

        g.sort()
        s.sort()
     
        cookie_index = 0
   
        for child_index, greed_factor in enumerate(g):
            # Skip cookies that are too small for current child
            while cookie_index < len(s) and s[cookie_index] < g[child_index]:
                cookie_index += 1
          
            # If we've run out of cookies, return number of satisfied children
            if cookie_index >= len(s):
                return child_index
          
            # Assign current cookie to current child and move to next cookie
            cookie_index += 1
      
     
        return len(g)



        