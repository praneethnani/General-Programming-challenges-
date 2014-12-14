class Solution:
    # @return a boolean
    def isValid(self, s):
        openBrac=set(['(','{','['])
        closedBrac=set([')','}',']'])
        bracDict={'(':')','{':'}','[':']'}
        openStack=[]
        for each in s:
            if each in openBrac:
                openStack.append(each)
            elif each in closedBrac:
                if len(openStack) <1:
                    return False
                brac=openStack.pop()
                if bracDict[brac] != each:
                    return False
        if len(openStack)>0:
            return False
        return True
                
        