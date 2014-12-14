class Solution:
    # @return a float
    def findMedianSortedArrays(self, A, B):
        if not A:
           return self.selfcalc(B)
        if not B:
           return self.selfcalc(A)
        else:
            return self.selfcalc(A+B)
    
    def selfcalc(self,newarr):
        length=len(newarr)
        newarr.sort()
        median=None
        if length ==1:
            return newarr[0]
        if length % 2 ==0:
            mid=length/2-1
            temp=newarr[mid]+newarr[mid+1]
            median=float(temp)/2
        else:
            mid=length/2
            median=float(newarr[mid])
        return median